
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

    text_list = text.split()

    if len(text_list) > 1:
        for i in range(len(text_list) - 1):
            if text_list[i] == ' ':
                text_list[i] = '-'

    fixed_text = ''

    for i in range(len(text_list)):
        if text_list[i] == ' ':
            continue
        fixed_text = fixed_text + text_list[i] + ' '

    if fixed_text[-1] == ' ':
        fixed_text = fixed_text[0: -1]

    return fixed_text
