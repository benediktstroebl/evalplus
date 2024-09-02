
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

    
    count = 0
    new_text = ""
    for i in text:
        if i == " ":
            count += 1
        else:
            if count > 2:
                new_text += "-"
                count = 0
                continue
            new_text += i
            count = 0
    return new_text
