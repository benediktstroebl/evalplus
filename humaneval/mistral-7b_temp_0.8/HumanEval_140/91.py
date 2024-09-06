
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
    a = text
    b = ""
    for i in range(len(a)):
        if i == 0 and a[i] != " ":
            b = b + a[i]
        if a[i] == " " and a[i+1] != " ":
            b = b + "_"
        if a[i] == " " and a[i+1] == " ":
            if i+2 < len(a) and a[i+2] != " ":
                b = b + "-"
            else:
                b = b + "_"
        if a[i] != " " and a[i+1] == " ":
            b = b + "_"
        if a[i] == " ":
            b = b + "_"
    return b
