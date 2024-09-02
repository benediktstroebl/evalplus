
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

    assert isinstance(text, str), 'Argument should be string'

    if len(text) == 0:
        return text

    if len(text) == 1:
        if text == ' ':
            return '_'
        return text

    new_text = text[0]
    for index in range(len(text) - 1):
        if text[index] == ' ' and text[index + 1] == ' ':
            new_text += '-'
        elif text[index] == ' ':
            new_text += '_'
        else:
            new_text += text[index]

    return new_text
