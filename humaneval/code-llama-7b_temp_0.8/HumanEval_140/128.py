
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
    return ''.join(['_' if '  ' in text else ' ' if len(text) == 0 else text[0],
                    *[('-' if (text[i+1] == ' ' and text[i] == ' ') else text[i+1]) 
                    for i in range(1, len(text))],
                    ['_' if text[-1] == ' ' else text[-1] if len(text) > 0 else ' '])







