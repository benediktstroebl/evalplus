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
    updated_text = ""
    last_char = ""
    consecutive_spaces = 0
    
    for char in text:
        if char == " ":
            consecutive_spaces += 1
        else:
            if consecutive_spaces > 2:
                updated_text += "-"
            elif consecutive_spaces > 0:
                updated_text += "_"
            updated_text += last_char * consecutive_spaces
            last_char = char
            consecutive_spaces = 0
    
    if consecutive_spaces > 2:
        updated_text += "-"
    elif consecutive_spaces > 0:
        updated_text += "_"
    updated_text += last_char * consecutive_spaces
    
    return updated_text
