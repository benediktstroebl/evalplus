
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
    for char in text:
        if char == ' ':
            new_text += '_'
        else:
            new_text += char

    if new_text.count(' ') > 2:
        idx = 0
        new_text = new_text.replace(' ', '-')
        while idx < len(new_text):
            if new_text[idx] == '-':
                new_text = new_text[:idx] + new_text[idx+1:]
            else:
                idx += 1
    
    return new_text

