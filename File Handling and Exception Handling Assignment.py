def read_and_modify_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the file name to read: ")

        # Open and read the file
        with open(filename, "r") as file:
            content = file.readlines()

        # Modify the content (Example: Convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content saved in '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
