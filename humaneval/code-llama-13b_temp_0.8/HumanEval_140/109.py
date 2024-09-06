
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
    if len(text) == 0:
        return ''

    new_text = []
    is_space = True if text[0] == ' ' else False

    for i in range(len(text)):
        if is_space:
            if i > 0 and text[i] != ' ':
                new_text.append('-')
                new_text.append(text[i])
                is_space = False
            elif text[i] == ' ':
                continue
            else:
                new_text.append('_')
                new_text.append(text[i])
                is_space = False
        else:
            if text[i] == ' ':
                is_space = True
                continue
            else:
                new_text.append(text[i])

    if is_space:
        new_text[-1] = '-'

    return ''.join(new_text)

