
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

    output = ""
    last_letter = ""
    has_space = False
    for letter in text:
        if letter == " ":
            if last_letter!= " ":
                has_space = True
        else:
            if has_space:
                output += "_"
            has_space = False
        output += letter
        last_letter = letter
    if last_letter == " ":
        output += "_"
    return output
    
