
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
    text_new = ""
    for i in range(0, len(text)-1):
        if text[i] == " ":
            text_new += "_"
        else:
            text_new += text[i]
    if text_new[len(text_new)-1] == " ":
        text_new += "_"
    else:
        text_new += text[len(text)-1]
    i = 0
    while (i+2) <= len(text_new)-1:
        if text_new[i] == " ":
            text_new = text_new[:i] + "-" + text_new[i+1:]
            i += 1
        i += 1
    return text_new
