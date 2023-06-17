import heapq
import graphviz
import time
import os


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class QueueNode:
    def __init__(self, node):
        self.node = node
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, node):
        new_node = QueueNode(node)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        node = self.front.node
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return node


def build_frequency_table(text):
    frequency_table = {}
    for char in text:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    return frequency_table


def build_huffman_tree(frequency_table):
    priority_queue = [Node(char, freq) for char, freq in frequency_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)
        combined_freq = left_node.freq + right_node.freq
        combined_node = Node(None, combined_freq)
        combined_node.left = left_node
        combined_node.right = right_node
        heapq.heappush(priority_queue, combined_node)

    return heapq.heappop(priority_queue)


def generate_huffman_codes(root):
    codes = {}

    def traverse(node, code):
        if node.char:
            codes[node.char] = code
            print(f"Character: {node.char} Huffman Code: {code}")
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(root, '')
    return codes


def compress_text(text, codes):
    compressed_text = ''.join(codes[char] for char in text)
    return compressed_text


def decompress_text(compressed_text, root):
    decompressed_text = []
    node = root
    for bit in compressed_text:
        node = node.left if bit == '0' else node.right
        if node.char:
            decompressed_text.append(node.char)
            node = root

    return ''.join(decompressed_text)


def build_tree_graph(root):
    graph = graphviz.Digraph()

    def add_node(node):
        if node.char:
            graph.node(str(id(node)), label=f"{node.char}:{node.freq}", shape="box")
        else:
            graph.node(str(id(node)), label=str(node.freq))

        if node.left:
            graph.edge(str(id(node)), str(id(node.left)), label="0")
            add_node(node.left)

        if node.right:
            graph.edge(str(id(node)), str(id(node.right)), label="1")
            add_node(node.right)

    add_node(root)
    return graph


def compress_and_decompress_text(text):
    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)
    huffman_codes = generate_huffman_codes(huffman_tree)

    compressed_text = compress_text(text, huffman_codes)
    decompressed_text = decompress_text(compressed_text, huffman_tree)

    return compressed_text, decompressed_text


def process_text(text):
    start_time = time.time()

    compressed_text, decompressed_text = compress_and_decompress_text(text)
    print("Compressed text (Huffman code):", compressed_text)
    print("Decompressed text:", decompressed_text)

    graph = build_tree_graph(build_huffman_tree(build_frequency_table(text)))
    graph.view()

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)


def main():
    # Choose mode (1 - Text input, 2 - File input)
    mode = input("Choose mode (1 - Text input, 2 - File input): ")

    if mode == "1":
        # Text input mode
        text = input("Enter the Persian text to process: ")
        process_text(text)
    elif mode == "2":
        # File input mode
        file_path = input("Enter the path of the file to process: ")
        if not os.path.isfile(file_path):
            print("Invalid file path!")
            return
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        process_text(text)
    else:
        print("Invalid mode!")


if __name__ == "__main__":
    main()