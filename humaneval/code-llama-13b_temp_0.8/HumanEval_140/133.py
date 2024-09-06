
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

    if len(text) == 0:
        return text
    
    text = text.split(" ")
    
    if len(text) == 1:
        return text[0]
    
    fixed_text = ""
    
    for i in range(len(text) - 1):
        if text[i] != "":
            fixed_text += text[i] + "_"
        else:
            if text[i + 1] != "":
                fixed_text += "-"
            else:
                fixed_text += "_"
    
    return fixed_text + text[-1]
