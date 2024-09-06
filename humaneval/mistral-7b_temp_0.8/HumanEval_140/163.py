
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

    string = ""
    for char in text:
        if char == " ":
            if string != "":
                if len(string) == 1:
                    string += "_"
                elif len(string) == 2:
                    string += "-"
            else:
                string += "_"
        else:
            string += char
    return string

