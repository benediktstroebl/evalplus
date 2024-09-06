
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
    if not isinstance(text, str):
        raise TypeError("text must be str")
    count = 0
    text_list = list(text)
    for i, x in enumerate(text_list):
        if x != ' ':
            count = 0
            continue
        if x == ' ':
            count += 1
            if count == 1:
                text_list[i] = '_'
            if count >= 2:
                text_list[i] = '-'
    text = "".join(text_list)
    return text

