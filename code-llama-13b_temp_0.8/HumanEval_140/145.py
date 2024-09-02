
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
        return ""

    if text == " ":
        return "_"

    result = ""
    space_counter = 0
    for i in range(len(text)):
        if text[i] == " ":
            space_counter += 1
        else:
            if space_counter == 0:
                result += text[i]
            elif space_counter == 1:
                result += "_"
            else:
                result += "-"
            space_counter = 0
    return result

