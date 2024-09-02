
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
    for c in text:
        if c == " ":
            output += "_"
        else:
            output += c
    # remove extra _
    while output.find("__") != -1:
        output = output.replace("_", " ", 1)
    # remove consecutive _s
    i = 1
    while output.find("_", i) != -1:
        output = output[0:output.find("_", i)] + output[output.find("_", i) + 1:]
        i += 1
    return output
