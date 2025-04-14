import os

def read_and_modify_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes the modified content to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    try:
        # Attempt to open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read the entire content of the input file
            file_content = infile.read()

            # Modify the content (example: convert to uppercase)
            modified_content = file_content.upper()  # Simple modification

        # Attempt to open the output file in write mode
        with open(output_filename, 'w') as outfile:
            # Write the modified content to the output file
            outfile.write(modified_content)

        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")
        return True  # Indicate success

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return False  # Indicate failure
    except IOError as e:
        print(f"IOError: An error occurred while reading or writing the file: {e}")
        return False  # Indicate failure
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False #Indicate failure

def main():
    """
    Main function to get user input, call the file processing function,
    and handle the overall program flow.
    """
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file to create: ")

    # Call the function to read, modify, and write the file
    success = read_and_modify_file(input_file, output_file)

    if success:
        print("File processing complete.")
    else:
        print("File processing failed.")
    print("Exiting Program.") #Added exit message

if __name__ == "__main__":
    main()

