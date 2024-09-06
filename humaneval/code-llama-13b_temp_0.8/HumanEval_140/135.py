
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
    text_list = []
    text_fixed = ''
    space_counter = 0

    for index in range(0, len(text)):
        if text[index] == ' ':
            text_list.append(text[index])
            space_counter += 1
        else:
            if space_counter == 1:
                text_list.append('_')
            elif space_counter > 2:
                text_list.append('-')
                space_counter = 0
            text_list.append(text[index])
            space_counter = 0

    for index in range(0, len(text_list)):
        text_fixed += text_list[index]

    return text_fixed
