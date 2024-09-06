
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
    string_len = len(text)
    for i in range(string_len):
        if text[i] == " ":
            if (i < string_len - 1) and (text[i + 1] == " "):
                new_string += "-"
            else:
                new_string += "_"
        else:
            new_string += text[i]
    return new_string

