
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
    text_1 = ""
    for i, char in enumerate(text):
        if text[i] == " ":
            if text[i-1] == " ":
                text_1 += "-"
            else:
                text_1 += "_"
        else:
            text_1 += char
    if text_1[0] == "_":
        text_1 = text_1[1:]
    return text_1
    pass
