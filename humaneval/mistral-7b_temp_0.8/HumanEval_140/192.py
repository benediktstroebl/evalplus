
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
    for char in text:
        if char != " ":
            new_string += char
        elif new_string == "" or new_string[-1] != " ":
            new_string += "_"
        elif new_string[-1] != " ":
            new_string += "-"

    return new_string

