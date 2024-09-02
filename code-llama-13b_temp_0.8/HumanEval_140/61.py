
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
    # print(text)
    new_str = ""
    if len(text) == 0:
        return text
    if text[0] == " ":
        new_str += "_"
    for i in range(len(text)):
        if text[i] == " ":
            if (i + 1) < len(text) and text[i + 1] == " ":
                new_str += "-"
            else:
                new_str += "_"
        else:
            new_str += text[i]
    return new_str
