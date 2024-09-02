
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
    if not text:
        return ""
    elif len(text) < 2:
        return text
    elif text.find(" ") == 0:
        return text[0:1] + text[1:].replace(" ", "_")
    elif text.find("   ") == 0:
        return text[0:2] + "_" + text[2:].replace("   ", "-")
    else:
        return text.replace(" ", "_")
