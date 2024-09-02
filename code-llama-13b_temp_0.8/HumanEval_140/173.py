
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
    new_text = ''
    text = text.replace(' ', '_')
    if len(text) > 2:
        for i in range(len(text)-1):
            if text[i] == '_' and text[i+1] == '_':
                new_text += '-'
            else:
                new_text += text[i]
        new_text += text[-1]
    return new_text
    
