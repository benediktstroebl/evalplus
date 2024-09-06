
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
    new_text = ""
    i = 0
    while i < len(text):
        if text[i] =='':
            new_text += '_'
            while text[i] =='':
                new_text += '_'
                i += 1
        elif i + 1 < len(text) and text[i + 1] =='':
            new_text += '-'
            i += 1
        else:
            new_text += text[i]
            i += 1
    return new_
