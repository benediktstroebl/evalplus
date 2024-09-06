
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
    text = text.replace(" ", "_")
    i = 0
    while i < len(text) - 1:
        if text[i] == "_" and text[i + 1] == "_":
            text = text[:i] + "-" + text[i + 1:]
            i += 1
        i += 1
    return text

