import sys
from linter import main

if __name__ == "__main__":
    print(sys.argv)
    print(len(sys.argv))
    if len(sys.argv) != 2:
        print("Usage: python linter.py <file_path>")
    else:
        main(sys.argv[1])