
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
        return text
    if len(text) == 1:
        if text == ' ':
            return '_'
        else:
            return text

    s = ""
    for i in range(len(text)):
        if text[i] == ' ' and i > 0 and text[i - 1] == ' ':
            s += '-'
        else:
            s += text[i]
    return s.replace(' ', '_')
