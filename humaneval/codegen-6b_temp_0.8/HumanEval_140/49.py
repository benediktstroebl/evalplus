
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
    if text == "":
        return ""
    if "  " not in text:
        return text
    new = ""
    # replace all consecutive spaces with -
    for s in text.split(" "):
        if new != "":
            new += "-"
        new += s
    # replace all spaces at the beginning and end of string
    while new.startswith(" "):
        new = new[1:]
    while new.endswith(" "):
        new = new[:-1]
    return new

