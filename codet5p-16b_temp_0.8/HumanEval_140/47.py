
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

    assert isinstance(text, str)
    if len(text) == 0:
        return text
    spaces_to_replace_with = '_'
    spaces_to_replace_with_2 = '-'
    new_text = ''
    current_index = 0
    for i in range(len(text)):
        if text[i] =='':
            current_index += 1
            if current_index > 2:
                new_text += spaces_to_replace_with
            else:
                new_text += spaces_to_replace_with_2
        else:
            new_text += text[i]
            current_index = 0
    return new_text
    
    
