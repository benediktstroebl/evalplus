
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

    
    new_string = ""
    space = " "
    consecutive_space = 0
    
    for i in range(len(text)):
        if text[i] == space:
            if consecutive_space == 2:
                consecutive_space = 0
                new_string += "_"
            else:
                consecutive_space += 1
        else:
            consecutive_space = 0
            new_string += text[i]
    
    return new_string
