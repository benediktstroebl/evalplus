
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
    space = 0
    for i, c in enumerate(text):
        if c == " ":
            space += 1
        elif c != " ":
            if space == 1:
                text = text[:i - 1] + "_" + text[i - 1:]
            elif space > 1:
                for j in range(space - 1):
                    text = text[:i - (j + 1)] + "-" + text[i - (j + 1):]
            space = 0

    return text

