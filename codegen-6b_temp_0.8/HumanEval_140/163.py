
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
    if text.replace(" ", "") == "":
        return "_"
    chars = []
    spaces = []
    for char in text:
        chars.append(char)
        if char == " ":
            spaces.append(1)
        else:
            spaces.append(0)
    chars = "".join(chars)
    spaces = "".join([str(space) for space in spaces])
    if spaces == "1111":
        return "_"+chars
    return chars.replace(" ", "_").replace("-", "_")
