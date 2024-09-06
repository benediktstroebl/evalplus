
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
    for i in range(len(text)):
        if text[i] == " ":
            if i != len(text) - 1:
                if text[i + 1] == " ":
                    text = text.replace("  ", "-")
                else:
                    text = text.replace(" ", "_")
            else:
                text = text.replace(" ", "_")
    return text

