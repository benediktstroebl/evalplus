
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
    # if text has no spaces, return the text
    if text.find(' ') == -1:
        return text
    # if the string has only a single space, return the string with the space replaced with underscore
    if text.find(' ') == 1:
        return text.replace(' ', '_')
    # replace spaces with underscore and do another loop
    # if the string has more than one space
    text = text.replace(' ', '_')
    while text.find('__') != -1:
        text = text.replace('__', '-')
    return text
