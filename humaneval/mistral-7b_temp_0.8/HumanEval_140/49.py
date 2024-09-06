
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
    # text_list = text.split(' ')
    # new_list = []
    # for elem in text_list:
    #     if elem.count(' ') > 2:
    #         new_list.append(elem.replace(' ', '-'))
    #     else:
    #         new_list.append(elem.replace(' ', '_'))
    # new_text = ''.join(new_list)
    # return new_text
    return text.replace(' ', '_').replace('  ', '-')


