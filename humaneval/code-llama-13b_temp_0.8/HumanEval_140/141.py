
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
    if len(text) == 0:
        return text

    start = 0
    end = len(text) - 1

    while start <= end and text[start] == ' ':
        start += 1
    
    while end >= 0 and text[end] == ' ':
        end -= 1
    
    if start > end:
        return ''

    text = text[start:end + 1]
    space_count = 0
    prev = ' '

    for idx, curr in enumerate(text):
        if curr == ' ' and prev == ' ':
            space_count += 1
        else:
            if space_count >= 2:
                text = text[:idx - 2] + '-' + text[idx:]
                space_count = 0
            elif space_count == 1:
                text = text[:idx - 1] + '_' + text[idx:]
                space_count = 0

        prev = curr

    if space_count >= 2:
        return '-' + text
    elif space_count == 1:
        return '_' + text

    return text

