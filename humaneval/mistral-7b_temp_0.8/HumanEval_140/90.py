
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
    last_space_index = 0
    for i, char in enumerate(text):
        if char == " ":
            if i == 0 or text[i - 1] != " ":
                output += char
                last_space_index = i
            elif i - last_space_index > 1:
                output += "-"
            elif i - last_space_index == 1:
                output += "_"
        else:
            output += char
    return output

