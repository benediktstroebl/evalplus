
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
    result = ""
    i = 0
    to_skip = 0
    while i < len(text):
        if text[i] == ' ':
            if to_skip > 0:
                to_skip -= 1
            else:
                result += '_'
        else:
            result += text[i]
            to_skip = 0
        i += 1
        
    if to_skip > 0:
        result += '-' * to_skip
        
    return result
