
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

    spaces = ' '
    length = len(text)
    count = 0
    for i in range(length):
        if text[i] == spaces:
            count += 1
            if count == 1:
                text = text.replace(spaces, '_', 1)
            elif count > 1 and count < 4:
                text = text.replace(spaces, '-', 1)
            else:
                text = text.replace(spaces, '-', 3)
                count = 0
    return text
