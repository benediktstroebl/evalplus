
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
    count_space = 0
    for el in text:
        if el == " ":
            count_space += 1
        else:
            if count_space == 1:
                res += "_"
            if count_space > 1:
                res += "-"
                count_space = 0
            res += el
    return res
