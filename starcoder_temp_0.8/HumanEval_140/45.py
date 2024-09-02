
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
    for letter in text:
        if letter == " ":
            if len(result) > 1 and result[-1] == "_":
                continue
            elif len(result) > 1 and result[-1] == "-":
                continue
            result += "-"
        else:
            result += letter
    return result

