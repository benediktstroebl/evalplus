
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
    # ...
    # for all spaces in text
    #   if more than 2 spaces, replace with -
    #   else, replace with _
    # ...
    result = ''
    for index, letter in enumerate(text):
        if letter == ' ':
            if text[index - 1] == ' ' and text[index - 2] == ' ':
                result += '-'
            else:
                result += '_'
        else:
            result += letter
    return result

