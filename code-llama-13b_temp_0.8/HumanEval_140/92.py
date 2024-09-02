
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
    for i, s in enumerate(text):
        if s == ' ':
            if new_text[-1] != ' ':
                new_text += '_'
            elif len(new_text) >= 2 and new_text[-2] == ' ':
                new_text = new_text[:-1] + '-'
        else:
            new_text += s
    return new_text
