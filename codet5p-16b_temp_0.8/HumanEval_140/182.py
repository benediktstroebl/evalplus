
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
    for i, char in enumerate(text):
        if char == " ":
            new_string += "_"
        else:
            new_string += char
    
    new_string2 = ""
    for i, char in enumerate(new_string):
        if new_string[i] == " " and new_string[i+1] == " ":
            new_string2 += "-"
        else:
            new_string2 += new_string[i]

    return new_string2
