
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
    # return "not implemented"
    # return 'not implemented'
    # return "not implemented"
    if not text:
        return text
    lst = list(text)
    is_underscore = False
    for i in range(len(text)):
        if text[i] == " ":
            if is_underscore:
                lst[i] = "-"
            else:
                lst[i] = "_"
            is_underscore = True
        else:
            is_underscore = False
    return ''.join(lst)

