
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

    new_text = ''
    for char in text:
        if char != ' ':
            new_text += char
        elif len(new_text) > 2:
            new_text += '-'
        else:
            new_text += '_'

    return new_text

