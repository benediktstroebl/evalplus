
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
    # if text is empty or text is None
    if not text:
        return ''

    # replace all spaces with underscores 
    text = text.replace(' ', '_')

    # split text with '_'
    text_splitted = text.split('_')

    # iterate through text_splitted and join if ' ' and > 2
    new_text = ''
    for i in range(len(text_splitted)):
        if text_splitted[i] == ' ' and len(text_splitted[i]) > 2:
            text_splitted[i] = '-'
        new_text += text_splitted[i]

    return new_text
