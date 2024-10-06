import re

# Function to read the contents of a file
def readfile(filepath):
    """Reads the content of the given file."""
    with open(filepath, 'r') as file:
        return file.read()

# Function to write content to a file
def writefile(filepath, content):
    """Writes the content to the given file."""
    with open(filepath, 'w') as file:
        file.write(content.strip() + '\n')  # Strip any extra whitespace/newlines

# Function to apply transformations
def apply_transformations(original_code):
    """
    Applies transformation rules to the original code.
    Transforms `turnHeading(value)` to `chassis.pid_turn_set(value_degree, 127)`
    and `driveDist(value)` to `chassis.pid_drive_set(value_inch, 100)`.
    """
    # Replace turnHeading with chassis.pid_turn_set
    transformed_code = re.sub(r'turnHeading\(([^)]+)\)', r'chassis.pid_turn_set(\1_degree, 127)', original_code)
    
    # Replace driveDist with chassis.pid_drive_set
    transformed_code = re.sub(r'driveDist\(([^)]+)\)', r'chassis.pid_drive_set(\1_inch, 100)', transformed_code)
    
    return transformed_code

# Main function
def main(original_file, refined_file):
    # Step 1: Read the original code from original.txt
    original_code = readfile(original_file)

    # Step 2: Apply the transformations to the original code
    refined_code = apply_transformations(original_code)

    # Step 3: Write the refined code to refined.txt
    writefile(refined_file, refined_code)

    print(f"Refined code has been saved to {refined_file}")

# Example usage
if __name__ == "__main__":
    #original_file = 'original.txt'  # The file containing the original code
    #refined_file = 'refined.txt'  # The file where the refined code will be saved
    original_file = 'C:/Users/user/Desktop/LunarUtil/codeConverter/originalC.txt'
    refined_file = 'C:/Users/user/Desktop/LunarUtil/codeConverter/refinedC.txt'
    
    # Call the main function to process the files
    main(original_file, refined_file)
