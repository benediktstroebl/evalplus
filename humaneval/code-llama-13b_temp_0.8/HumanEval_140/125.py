
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
    if not text:
        return text
    # adding underscore before first word
    if text[0] == ' ':
        text = '_' + text[1:]
    # replacing multiple spaces
    if '  ' in text:
        text = text.replace('  ', ' ')
        text = fix_spaces(text)
    # replacing single spaces with underscore
    if ' ' in text:
        text = text.replace(' ', '_')
    return text

