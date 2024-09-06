
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
    subs = {}
    subs[" "] = "_"
    for i in subs:
        text = text.replace(i, subs[i])
    if len(text) > 2:
        for i in range(0, len(text) - 1):
            if text[i:i + 2] == "  ":
                text = text[0:i] + "_" + text[i + 2:]
        text = text.replace("   ", "_")
    return text

