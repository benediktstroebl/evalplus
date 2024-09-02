
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
    if text == '':
        return ''

    first_char = text[0]
    last_char = text[-1]
    text = text.strip()
    if len(text) < 2:
        return first_char + text.replace(' ', '_') + last_char

    new_text = text.split()
    first_part = new_text[0]
    last_part = new_text[-1]
    new_text = new_text[1:-1]

    new_text = [first_part] + [x.replace(' ', '_') for x in new_text] + [last_part]

    if len(new_text) == 1:
        return first_char + new_text[0] + last_char

    new_text = [new_text[0]] + [x.replace('  ', '-') for x in new_text[1:-1]] + [new_text[-1]]

    return first_char + ' '.join(new_text) + last_char
