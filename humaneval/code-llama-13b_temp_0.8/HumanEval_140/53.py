
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
    # return text.replace(' ', '_')
    if len(text) == 0:
        return ''
    
    if text[0] != ' ':
        return text[0] + fix_spaces(text[1:])
    
    if len(text) < 3:
        return '-' + fix_spaces(text[1:])
    
    if text[0:2] != '  ':
        return '_' + fix_spaces(text[1:])
    
    if text[2] != ' ':
        return '_' + text[2] + fix_spaces(text[3:])
    
    if text[0:3] != '   ':
        return '-' + fix_spaces(text[1:])
    
    return '-' + fix_spaces(text[3:])
    
