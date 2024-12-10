def read_and_write_file():
    try:
        # Ask the user for the filename
        input_filename = input("Enter the file to read: ").strip()
        
        # Read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        output_filename = input("Enter the file to save the modified content: ").strip()
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Content saved to {output_filename}!")
    
    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
read_and_write_file()
