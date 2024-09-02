
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
    # pass
    if text == None:
        return None
    if len(text) == 0:
        return text
    res = ""
    count_spaces = 0
    for letter in text:
        if letter == " ":
            count_spaces += 1
        if count_spaces >= 3 and letter == " ":
            res += "-"
            count_spaces = 0
        else:
            if letter != " ":
                count_spaces = 0
                res += letter
            else:
                res += "_"
    return res

