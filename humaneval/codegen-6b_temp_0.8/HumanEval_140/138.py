
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

    temp = text[:]
    temp = temp.replace(" ", "_")
    temp = temp.replace("  ", "_")
    temp = temp.replace("   ", "_")

    if temp[0] == "_":
        temp = temp[1:]

    if temp[-1] == "_":
        temp = temp[:-1]

    return temp
