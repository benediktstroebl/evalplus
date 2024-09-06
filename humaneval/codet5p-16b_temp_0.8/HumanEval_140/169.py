
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

    
    if text == "":
        return ""
    
    consecutive_spaces = 1
    new_text = ""
    for i in range(len(text)):
        if text[i] == " ":
            if i == len(text) - 1:
                consecutive_spaces -= 1
            else:
                consecutive_spaces = 1
            
            if consecutive_spaces == 0:
                new_text += "_"
            elif consecutive_spaces > 2:
                new_text += "_"
            else:
                new_text += "-"
        else:
            consecutive_spaces = 0
            new_text += text[i]
    return new_text
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
