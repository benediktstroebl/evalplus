
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
    counter = 0
    for i in range(len(text)):
        if text[i] == " ":
            if counter > 1:
                result += "_"
            else:
                result += text[i]
        else:
            result += text[i]
        counter += 1
    return result

