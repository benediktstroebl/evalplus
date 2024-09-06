
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
    s = ""
    count = 0
    for i in range(len(text)):
        if text[i] == " " and count == 0:
            s += "_"
        elif text[i] == " " and count > 0:
            s += "-"
        else:
            s += text[i]
            count = 0
        if text[i] == " ":
            count += 1
    return s

