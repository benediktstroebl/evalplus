
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
    s = str(text)
    l = list(s)
    s = ""
    if len(l) > 0:
        if l[0] == " ":
            l[0] = "_"
        for i in range(len(l)):
            if i > 0:
                if l[i] == " ":
                    if l[i - 1] == "_":
                        l[i] = "-"
                    else:
                        l[i] = "_"
    for i in l:
        s += i
    return s
