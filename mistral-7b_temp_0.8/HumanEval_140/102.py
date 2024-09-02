
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
    fix_spaces = " "
    res_spaces = ""

    for i in range(len(text)):
        if text[i] == " ":
            if text[i-1] == " " and text[i+1] == " ":
                res_spaces += "-"
            else:
                res_spaces += "_"
        else:
            res_spaces += text[i]
    return res_spaces
