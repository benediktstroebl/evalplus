
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
    # if len(text) == 0 or text.find(' ') == -1:
    #     return text
    #
    # new_str = text.replace(' ', '_')
    # while new_str.find('__') != -1:
    #     new_str = new_str.replace('__', '_')
    #
    # return new_str

    new_str = text.replace(' ', '_')
    new_str = new_str.replace('__', '_')
    return new_str

