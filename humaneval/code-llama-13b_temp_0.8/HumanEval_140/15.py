
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
    if len(text) == 1:
        return text.replace(' ', '_')
    if text[0] == ' ':
        text = '_' + text[1:]
    if text[-1] == ' ':
        text = text[:-1] + '_'
    text = text.replace('  ', ' ')
    return text.replace(' ', '_')

    pass
