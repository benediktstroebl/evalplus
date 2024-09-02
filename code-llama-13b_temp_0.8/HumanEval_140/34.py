
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
    if text == '':
        return text
    if text[-1].isspace():
        return fix_spaces(text[:-1]) + '-'
    if text[0].isspace():
        return '_' + fix_spaces(text[1:])
    return text if text.find('  ') == -1 else fix_spaces(text.replace('  ', '_'))
