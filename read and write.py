"""
File Handling and Exception Handling Assignment
------------------------------------------------
Task 1: File Read & Write Challenge
    - Read a file
    - Write a modified version to a new file
Task 2: Error Handling Lab
    - Ask the user for a filename
    - Handle errors if the file doesn’t exist or can’t be read
"""

def read_and_modify_file(input_file, output_file):
    """Reads input_file, modifies content, and writes to output_file."""
    try:
        with open(input_file, "r") as infile:
            content = infile.read()
            print("\n✅ Original file content read successfully!")

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)
            print(f"✅ Modified content written to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read/write files.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


def main():
    print("📂 File Handling and Exception Handling Program")
    filename = input("Enter the name of the file to read: ")
    output = "modified_output.txt"

    read_and_modify_file(filename, output)


if __name__ == "__main__":
    main()
