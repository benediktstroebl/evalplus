
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
    i = 0
    while i < len(text):
        if text[i] == ' ':
            text = text[0:i] + '_' + text[i+1:]
            i += 1
        i += 1
    
    if len(text) > 2:
        while i < len(text):
            if text[i] == ' ' and text[i+1] == ' ':
                text = text[0:i+1] + '-' + text[i+2:]
            i += 1
    return text

