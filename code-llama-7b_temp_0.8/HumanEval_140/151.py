
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
    if text.find("  ") == -1:
        return text.replace(" ", "_")
    else:
        # Create a copy of the original string to avoid changing it in the original 
        # string
        temp_text = text[:]
        # Search the string for double spaces
        temp_text = temp_text.replace("  ", "-")
        # Change remaining spaces to underscores
        temp_text = temp_text.replace(" ", "_")
        return temp_text
