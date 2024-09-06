
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
    prev_space = False
    prev_dash = False
    for character in text:
        if character == " ":
            if prev_space or prev_dash:
                new_text += "_"
            else:
                new_text += character
            prev_space = False
            prev_dash = False
        elif character == "-":
            if prev_space or prev_dash:
                new_text += "_"
            else:
                new_text += character
            prev_space = False
            prev_dash = True
        else:
            new_text += character
            prev_space = True
            prev_dash = False

    return new_text
