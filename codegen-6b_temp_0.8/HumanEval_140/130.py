
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

    for index in range(len(text_list)):
        if text_list[index] == " ":
            text_list[index] = "_"
        elif index < len(text_list) - 1:
            if text_list[index] == " " and text_list[index + 1] == " ":
                text_list[index] = "_"

    return "".join(text_list)
