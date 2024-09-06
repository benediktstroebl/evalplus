
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
    space_count = 0
    for el in text:
        if el == ' ':
            space_count += 1
            if space_count == 2:
                res += '-'
            else:
                res += '_'
        else:
            res += el
            space_count = 0
    if res[0] == ' ':
        res = res[1:]
    return res
