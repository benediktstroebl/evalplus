
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
    i = 0
    new_text = ""
    while i < len(text):
        if text[i] == ' ':
            new_text += "_"
            i += 1
        else:
            new_text += text[i]
            i += 1
    fixed_text = new_text.replace("_", " ")
    if "_" in fixed_text:
        fixed_text = fixed_text.replace("_", " ")
    return fixed_text
