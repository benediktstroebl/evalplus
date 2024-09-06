
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
    # return text.replace(' ', '_').replace('  ', '-')
    # or
    if len(text) == 0:
        return text
    elif text[0] == ' ':
        return '_' + fix_spaces(text[1:])
    elif len(text) > 1:
        if text[:2] == '  ':
            return '-' + fix_spaces(text[2:])
        else:
            return text[:1] + fix_spaces(text[1:])
    else:
        return text

