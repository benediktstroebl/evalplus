
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
    for c in text:
        if c == " ":
            new_string += "_"
        else:
            new_string += c
    
    new_string_2 = new_string
    for i in range(len(new_string_2)):
        if new_string_2[i] == "_":
            if new_string_2[i+1] == "_":
                new_string_2 = new_string_2[:i] + "-" + new_string_2[i+2:]
    
    return new_string_2
