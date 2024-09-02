
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
    assert isinstance(text, str), 'Should be string'
    
    if len(text) == 0:
        return text
    
    new_text = text[0]
    new_text = new_text.replace(' ', '_')
    
    for i in range(1, len(text)):
        if text[i] == ' ':
            if text[i - 1] == ' ':
                new_text += '-'
            else:
                new_text += '_'
        else:
            new_text += text[i].replace(' ', '_')
    
    return new_text

