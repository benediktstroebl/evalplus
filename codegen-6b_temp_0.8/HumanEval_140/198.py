
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
    fixed_spaces = ''
    for ch in text:
        if ch == ' ':
            fixed_spaces += '_'
        elif ch == '  ':
            fixed_spaces += '-'
        else:
            fixed_spaces += ch
    return fixed_spaces
