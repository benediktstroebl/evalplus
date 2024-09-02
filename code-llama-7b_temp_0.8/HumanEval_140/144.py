
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
    
    new_text = text.split()
    i = 0
    while i < len(new_text):
        if len(new_text[i]) > 1:
            new_text[i] = '_'.join(new_text[i].split())
            i += 1
        elif len(new_text[i]) == 1 and new_text[i].isspace():
            new_text[i] = '_'
            i += 1
        elif len(new_text[i]) == 1 and not new_text[i].isspace():
            i += 1
    
    return ' '.join(new_text)
