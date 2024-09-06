
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # Create a set of characters that we will replace with a dash
    dash_chars = "-"
    
    # Create a list to store the fixed string
    fixed_text = []
    
    # Loop through the characters in the string
    for char in text:
        # If the character is a space or a dash
        if char in [" ", dash_chars]:
            # Replace the character with a dash
            fixed_text.append(dash_chars)
        else:
            # Add the character to the fixed string
            fixed_text.append(char)
    
    return " ".join(fixed_text)
