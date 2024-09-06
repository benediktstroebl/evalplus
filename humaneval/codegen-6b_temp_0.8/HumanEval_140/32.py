
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
    # We want to replace all spaces in the string with underscores
    text = text.replace(" ", "_")
    
    # If the string has more than 2 consecutive spaces, we replace them
    # with a "-"
    if "  " in text:
        text = text.replace("  ", "-")
    
    return text