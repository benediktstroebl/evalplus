
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
    for c in text:
        if c == " ":
            c = "_"
        s += c
    
    # If there are more than 2 spaces in a row, replace them with a -
    while "_"*3 in s:
        s = s.replace("_"*3, "-")
    
    return s
