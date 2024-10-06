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

# Function to mirror turn angles by flipping the sign
def mirror_turns(code):
    """
    This function mirrors turn angles by flipping their sign.
    E.g., 90_deg becomes -90_deg, and -45_deg becomes 45_deg.
    """
    # Use regex to find patterns with degrees and flip the sign
    def flip_degree(match):
        degree_value = float(match.group(1))
        flipped_value = -degree_value  # Flip the degree value
        return f"{flipped_value}_deg"

    # Flip all turn degrees in pid_turn_set and pid_turn_relative_set
    code = re.sub(r'([+-]?\d+\.?\d*)_deg', flip_degree, code)
    return code

# Function to convert negRed to negBlue
def convert_neg_red_to_neg_blue(original_code):
    """
    Converts negRed function into negBlue by mirroring turn angles.
    """
    # Step 1: Replace the function name
    mirrored_code = original_code.replace("void negRed", "void negBlue")

    # Step 2: Mirror the turn angles
    mirrored_code = mirror_turns(mirrored_code)

    return mirrored_code

# Main function
def main(original_file, refined_file):
    # Step 1: Read the original code from originalM.txt
    original_code = readfile(original_file)

    # Step 2: Convert negRed to negBlue
    mirrored_code = convert_neg_red_to_neg_blue(original_code)

    # Step 3: Write the mirrored code to refinedM.txt
    writefile(refined_file, mirrored_code)

    print(f"Mirrored code has been saved to {refined_file}")

# Example usage
if __name__ == "__main__":
    #original_file = 'originalM.txt'  # The file containing the original code (negRed)
    #refined_file = 'refinedM.txt'  # The file where the mirrored code (negBlue) will be saved
    original_file = 'C:/Users/user/Desktop/LunarUtil/codeMirror/originalM.txt'
    refined_file = 'C:/Users/user/Desktop/LunarUtil/codeMirror/refinedM.txt'
    # Call the main function to process the files
    main(original_file, refined_file)
