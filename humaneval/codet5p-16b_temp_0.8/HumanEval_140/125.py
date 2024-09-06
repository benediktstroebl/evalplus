
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

    
    return_text = ""
    for i in range(len(text)):
        if text[i] == " ":
            return_text += "_"
        else:
            return_text += text[i]
    
    return_text_temp = return_text
    return_text = ""
    for i in range(len(return_text_temp)):
        if i < len(return_text_temp)-1 and return_text_temp[i+1] == " ":
            return_text += "_"
        else:
            return_text += return_text_temp[i]
    
    return return_text

