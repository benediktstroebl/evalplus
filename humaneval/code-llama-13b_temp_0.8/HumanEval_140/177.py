
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
    space = 0
    text = text.replace(' ', '_')
    
    for i in range(len(text)):
        if text[i] == '_' and text[i+1] == '_':
            space += 1
        else:
            space = 0
        if space == 2:
            text = text[:i] + '-' + text[i+1:]
            space = 0
        
    if text[0] == '_':
        text = text[1:]
    if text[-1] == '_':
        text = text[:-1]
    
    return text

