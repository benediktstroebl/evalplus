
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
    elif len(text) == 1:
        return "_"+text[0]+"_"
    elif len(text) == 2:
        return "_"+text
    else:
        if text[1] == " ":
            return "_"+text[0]+text[2:]+"_"
        else:
            return text
            
