
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
    if not isinstance(text, str):
        return False
    res = ""
    counter = 0
    for i in text:
        if i == " ":
            counter += 1
            continue
        if counter > 2:
            if res[-1] == "-":
                res = res[:-1]
            res += "-"
            counter = 0
        else:
            if counter != 0:
                res += "_"
            counter = 0
        res += i
    return res

