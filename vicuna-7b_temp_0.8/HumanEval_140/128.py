
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
    underscores = "_"
    spaces = " "
    ret = ""
    last_space = True
    for char in text:
        if char == spaces:
            if last_space:
                last_space = False
            else:
                ret += spaces
        elif char == underscores:
            ret += char
            last_space = True
        else:
            ret += char
            last_space = False
        if len(text) - len(ret) >= 2 and ret[-2] == spaces and ret[-1] == spaces:
            ret += "-"
            last_space = True
    return ret.strip()
