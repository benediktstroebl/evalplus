
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
    if ' ' not in text:
        return text
    result = ''
    temp = ''
    for i in text:
        if i == ' ':
            if len(temp) != 0:
                result = result + temp
                temp = ''
        else:
            temp = temp + i
    if len(temp) != 0:
        result = result + temp
    
    result = result.replace("  ", "-")
    return result

