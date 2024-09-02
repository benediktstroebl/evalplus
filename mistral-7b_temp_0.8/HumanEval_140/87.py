
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
    new_text = ''
    new_text_list = []
    text_list = text.split(' ')
    for i in range(len(text_list)):
        if len(text_list[i]) == 1:
            new_text_list.append(text_list[i])
        elif text_list[i] == ' ':
            new_text_list.append('_')
        else:
            new_text_list.append('-')
    new_text = ''.join(new_text_list)
    return new_text

