
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
    # Remove whitespace at the start and the end of a string
    new_text = text.strip()
    
    # Replace all spaces in the string with an underscore
    new_text = new_text.replace(' ', '_')
    
    # Replace all the dashes with a space
    new_text = new_text.replace('-', ' ')
    
    # If we have more than 2 consecutive spaces, replace all the spaces with a dash
    new_text = new_text.replace('  ', '-')
    
    # Return the fixed string
    return new_text
