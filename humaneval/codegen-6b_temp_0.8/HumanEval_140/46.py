
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
    # put a space at the beginning of text, and remove all spaces
    fixed_text = text.strip().strip('_')
    
    # find the first space
    i = 0
    while i < len(fixed_text) and fixed_text[i] != ' ':
        i += 1

    # if the string is empty, return it as is
    if i == len(fixed_text):
        return text
    
    # if the string has only one space, then add an underscore
    if i == len(fixed_text)-1:
        return fixed_text + '_'
    
    # if the string has more than two consecutive space, add an underscore and replace consecutive spaces with an hyphen
    if i != 0 and fixed_text[i-1] == ' ':
        return fixed_text[:i] + '_' + fixed_text[i:]
    
    return fixed_text
