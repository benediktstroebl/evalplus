
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
    result = text
    if len(text) == 0:
        return ""
    if text == "":
        return ""
    if text.startswith(" ") and text.endswith(" "):
        result = "_"

    if "  " in text:
        while "  " in text:
            text = text.replace("  ", " - ")
    if "   " in text:
        while "   " in text:
            text = text.replace("   ", " -")
    return result
    