
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
    res = ""
    space = False
    for i in range(len(text)):
        if text[i] == " " and not space:
            res += "_"
            space = True
        elif text[i] == "_":
            space = False
        else:
            res += text[i]

    if space:
        if len(text) > 2:
            res = res[0] + res[2:]
        else:
            res = res[0] + res[1]

    return res

