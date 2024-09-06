
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
    #raise NotImplementedError

    if len(text) == 0:
        return ''
    result = []
    result.append(text[0])

    if text[0] == ' ':
        result[0] = '_'
    else:
        result[0] = text[0]

    for i in range(1, len(text)):
        if text[i] == ' ':
            if text[i - 1] == ' ':
                result.append('-')
            else:
                result.append('_')
        else:
            result.append(text[i])
    return ''.join(result)

