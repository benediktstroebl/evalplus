
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
    for i, letter in enumerate(text):
        if i == 0:
            new_text += letter
        elif text[i] == " " and text[i-1] == " ":
            new_text += "_"
        else:
            new_text += letter
    
    if "  " in new_text:
        new_text = fix_spaces("_".join(new_text.split()))
    
    return new_text


