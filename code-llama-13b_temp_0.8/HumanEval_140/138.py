
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
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    if len(text) == 0:
        return ''
    if len(text) == 1:
        return text if text != ' ' else '_'
    if len(text) == 2:
        return text.replace(' ', '_')
    else:
        text = text.replace(' ', '_')
        while '__' in text:
            text = text.replace('__', '_')
        if '  ' in text:
            return text.replace('  ', ' -')
        return text
    
    pass

