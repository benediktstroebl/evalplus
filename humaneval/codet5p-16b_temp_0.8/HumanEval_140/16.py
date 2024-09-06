
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

    
    prev_char = ""
    new_text = ""
    
    for char in text:
        if char == " ":
            new_text += "_"
            prev_char = ""
            continue
        if prev_char == " " and char == " ":
            new_text += "_"
        else:
            new_text += char
            prev_char = char
    
    return new_text
