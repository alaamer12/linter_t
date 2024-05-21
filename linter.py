import ast
import sys

MAX_LINE_LENGTH = 80

def check_line_length(lines):
    errors = []
    for i, line in enumerate(lines):
        if len(line) > MAX_LINE_LENGTH:
            errors.append((i + 1, f"Line too long ({len(line)} characters)"))
        print("No Errors")
    return errors

def check_unused_imports(lines):
    tree = ast.parse("".join(lines))
    errors = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.asname:
                    name = alias.asname
                else:
                    name = alias.name
                if not any(name in line for line in lines):
                    errors.append((node.lineno, f"Unused import '{name}'"))
                # print("No Errors")
    return errors

def main(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    errors = []
    errors.extend(check_line_length(lines))
    errors.extend(check_unused_imports(lines))

    for line_num, message in sorted(errors):
        print(f"{file_path}:{line_num}: {message}")
    print("done")

if __name__ == "__main__":
    print(sys.argv)
    print(len(sys.argv))
    if len(sys.argv) != 2:
        print("Usage: python linter.py <file_path>")
    else:
        main(sys.argv[1])
