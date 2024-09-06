
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

    
    count = 0
    consecutive = False
    result = ""
    for i in text:
        if i == " ":
            result += "_"
            consecutive = False
            count = 0
        elif i == " " and count > 2 and not consecutive:
            result += "-"
            consecutive = True
        else:
            result += i
            consecutive = False
        count += 1
    return result

