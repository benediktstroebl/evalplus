
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
    new_text = text.replace(' ', '_')
    spaces = 0
    new_string = ''
    for char in new_text:
        if char == ' ':
            spaces += 1
            if spaces >= 2:
                new_string += '-'
            else:
                new_string += '_'
        else:
            new_string += char
            spaces = 0

    return new_string

