
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
    for char in text:
        if char == " ":
            if len(text) > 1 and text[0] == " " and text[1] == " ":
                result += text[0] + "-"
                text = text[1:]
            else:
                result += "_"
        else:
            result += char
    return result
