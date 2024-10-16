#!/usr/bin/env python3
import sys

def count_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            return len(file.read())
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def ccwc():
    if len(sys.argv) != 3:
        print("Usage: ccwc [-c:byte count|-l: line count] <filename>")
        return
    
    option = sys.argv[1]
    file_path = sys.argv[2]

    if option == '-c':
        byte_count = count_bytes(file_path)
        if byte_count is not None:
            print(f"{byte_count} {file_path}")
    elif option == '-l':
        line_count = count_lines(file_path)
        if line_count is not None:
            print(f"{line_count} {file_path}")
    else:
        print(f"Unknown option: {option}")

if __name__ == "__main__":
    ccwc()
