
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
    result = []
    prev_space = False
    prev_index = 0
    for index, letter in enumerate(text):
        if letter == ' ':
            if prev_space:
                result.append('-')
                prev_index += 1
            else:
                result.append('_')
                prev_space = True
                prev_index = index
        else:
            prev_space = False
            result.append(letter)
    return ''.join(result)

