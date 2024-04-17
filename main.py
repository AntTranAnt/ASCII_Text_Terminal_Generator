import sys

def main():
    # Input validation
    if len(sys.argv) != 2:
        print("Format: python main.py input_file")
        return
    inputFile = sys.argv[1]
    if not inputFile.endswith(".txt"):
        print("Only input .txt files")
        return

    # Script to print file
    generated_script = """def main():\n"""

    # Read in file
    with open(inputFile, 'r') as file:
        for line in file:
            line = line.rstrip()
            line = line.replace("\\", "\\\\")
            line = line.replace("\"", "\\\"")
            generated_script += "\tprint(\"" + line + "\")\n"
    
    # Write out to new .py file
    generated_script += "\nif __name__ == \"__main__\":\n"
    generated_script += "\tmain()"
    inputFile = inputFile[:-4]
    fileTitle = f"output/{inputFile}.py"

    with open(fileTitle, "w") as file:
        file.write(generated_script)


if __name__ == "__main__":
    main()