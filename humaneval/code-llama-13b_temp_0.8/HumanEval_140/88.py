
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
    if len(text) == 0:
        return ""

    index = 0
    while text[index] == " ":
        index += 1
    if index == len(text):
        return ""
    elif index > 0:
        text = "_" + text[index:]

    output = ""
    prev_space = False
    double_space = False
    prev_prev_space = False
    for c in text:
        if c == " ":
            if prev_space and not prev_prev_space:
                double_space = True
            elif prev_space and prev_prev_space:
                output += "-"
            else:
                output += "_"
            prev_space = True
            prev_prev_space = False
        else:
            output += c
            prev_space = False
            prev_prev_space = prev_space
            double_space = False

    if double_space:
        output = output[:-1]

    return output
