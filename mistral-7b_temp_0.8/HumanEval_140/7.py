
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
    str_list = list(text)
    new_str_list = []
    for elem in str_list:
        if elem == ' ' and len(str_list) >= 3 and str_list[str_list.index(elem)+1] == ' ':
            new_str_list.append('-')
        else:
            new_str_list.append(elem)
    return ''.join(new_str_list)
