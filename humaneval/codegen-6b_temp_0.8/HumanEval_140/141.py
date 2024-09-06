
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
    text_list = list(text)
    has_space = False
    spaces_to_replace = 0
    for i in range(len(text_list)-1):
        if text_list[i] == " " and text_list[i+1] == " ":
            has_space = True
            spaces_to_replace += 1
        else:
            if has_space:
                text_list[i-(spaces_to_replace*2)] = "_"
                text_list[i-(spaces_to_replace*2)+1] = "_"
            has_space = False
    
    text = "".join(text_list)
    return text
