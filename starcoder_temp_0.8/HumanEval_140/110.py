
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
    new_string = []
    for i in text.split(" "):
        new_string.append(i.replace(" ", "_"))
    new_string = [i.replace("__", "_") for i in new_string]
    new_string = [i.replace("__", "_") for i in new_string]
    new_string = "-".join(new_string)
    return new_string
