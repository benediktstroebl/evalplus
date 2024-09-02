
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
    consecutive_spaces = 0
    for c in text:
        if c == " ":
            result += "_"
            consecutive_spaces += 1
        else:
            if consecutive_spaces >= 2:
                result += "-".join("_" for _ in range(consecutive_spaces))
                consecutive_spaces = 0
            result += c
    if consecutive_spaces >= 2:
        result += "-".join("_" for _ in range(consecutive_spaces))
    return result
