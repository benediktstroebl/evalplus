
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
    new_text = ""
    i = 0
    while i < len(text):
        char = text[i]
        if char == " ":
            if text[i:i+2] == "  ":
                new_text += "-"
            else:
                new_text += "_"
        else:
            new_text += char
        i += 1
    return new
