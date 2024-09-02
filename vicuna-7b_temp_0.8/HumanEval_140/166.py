
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
    # count the number of spaces in the string
    n_spaces = len(text) - len(text.lstrip(' '))
    
    # replace all spaces with underscores
    return ' '.join([text[i:i+n_spaces] for i in range(0, len(text), n_spaces)])
