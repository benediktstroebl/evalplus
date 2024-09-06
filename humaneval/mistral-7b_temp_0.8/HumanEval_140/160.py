
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
    result = ""
    space_flag = False
    for i, letter in enumerate(text):
        if letter == " ":
            if i == 0 or i == len(text)-1:
                space_flag = True
            elif space_flag:
                result += "-"
            else:
                result += "_"
        else:
            space_flag = False
            result += letter
    return result
