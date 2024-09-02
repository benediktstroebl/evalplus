
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

    
    new_text = ""
    spaces = 0
    
    for i in range(len(text)):
        if text[i] == " ":
            spaces += 1
            if spaces > 2:
                new_text += "_"
            else:
                new_text += "-"
        else:
            new_text += text[i]
            spaces = 0
    
    return new_text
    
