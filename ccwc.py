#!/usr/bin/env python3
import sys

def count_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:  # Open file in binary mode
            byte_count = len(file.read())  # Count bytes by reading the file
        return byte_count
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def ccwc():
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ccwc -c <filename>")
        return
    
    option = sys.argv[1]
    file_path = sys.argv[2]

    if option == '-c':  # Count bytes option
        byte_count = count_bytes(file_path)
        if byte_count is not None:
            print(f"{byte_count} {file_path}")
    else:
        print(f"Unknown option: {option}")

if __name__ == "__main__":
    ccwc()
