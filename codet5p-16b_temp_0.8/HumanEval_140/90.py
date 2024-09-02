
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

    spaces = 0
    for index in range(len(text)):
        if text[index] == " ":
            spaces += 1
    if spaces > 2:
        new_string = ""
        for index in range(len(text)):
            if text[index] == " ":
                new_string += "_"
            else:
                new_string += text[index]
        return new_string
    else:
        return text
