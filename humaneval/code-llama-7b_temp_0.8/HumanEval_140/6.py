
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
    text = text.replace(" ", "_")
    new_text = ""
    
    for i in text:
        if i == "_":
            count = 1
            new_text += "_"
            continue
        else:
            if count >= 3:
                new_text += "-"
            else:
                new_text += i

    return new_text
