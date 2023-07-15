  # Huffman Coding Program

This is a Python program that implements Huffman coding, a lossless data compression algorithm. The program allows you to compress and decompress text using Huffman coding. It provides two modes: text input mode and file input mode.

## How Huffman Coding Works**
Huffman coding is a variable-length prefix coding algorithm that assigns shorter codes to more frequent characters and longer codes to less frequent characters. This allows for efficient compression of data by representing frequently occurring characters with fewer bits.

The program follows the following steps to perform Huffman coding:
1. **Building the Frequency Table:** The program takes input text and builds a frequency table, which records the frequency of each character in the text.
2. **Building the Huffman Tree:** Using the frequency table, the program constructs a Huffman tree. It creates a priority queue of nodes, each representing a character and its frequency. It repeatedly combines the two nodes with the lowest frequencies into a new node until a single root node is created.
3. **Generating Huffman Codes:** Traversing the Huffman tree, the program generates Huffman codes for each character. The codes are binary strings assigned based on the path from the root to each leaf node.
4. **Compressing the Text:** The program compresses the input text by replacing each character with its corresponding Huffman code.
5. **Decompressing the Text:** The compressed text can be decompressed by traversing the Huffman tree based on the bits in the compressed text. The traversal follows '0' for the left child and '1' for the right child until a leaf node is reached. The character at the leaf node is appended to the decompressed text.
6. **Visualization:** The program also generates a visualization of the Huffman tree using the Graphviz library. The visualization helps to understand the structure of the tree and the assigned codes.

## Usage
The program provides two modes of operation: text input mode and file input mode.

## Text Input Mode
In text input mode, you can directly input the Persian text to be processed.

1. Run the program and choose "1" for text input mode.
2. Enter the Persian text to be processed when prompted.
3. The program will compress the text using Huffman coding, display the compressed text (Huffman code), and then decompress it to verify the accuracy.
4. Additionally, a visualization of the Huffman tree will be generated and displayed.

## File Input Mode
In file input mode, you can provide a file containing the Persian text to be processed.
1. Run the program and choose "2" for file input mode.
2. Enter the path of the file to be processed when prompted. Make sure the file exists and is encoded in UTF-8.
3. The program will read the text from the file, perform the compression and decompression, and display the results.
4. A visualization of the Huffman tree will also be generated and displayed.

## Dependencies
The program has the following dependencies:
1. **heapq:** Used to create a priority queue for building the Huffman tree.
2. **graphviz:** Used to generate the visualization of the Huffman tree.
3. **time: Used to measure the execution time of the program.
4. **os:** Used for file input mode to check the validity of the file path.

Make sure to install these dependencies before running the program. You can use pip to install them:
**"pip install heapq graphviz"**

## Conclusion
This Huffman coding program provides a simple and efficient way to compress and decompress text. By utilizing the frequency of characters, it generates optimal variable-length codes, resulting in effective data compression. Feel free to use and modify the code according to your needs.
