
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
    spaces = text.find(" ")
    if spaces == -1:
        return text
    else:
        start = spaces
        spaces = text.find(" ", start + 1)
        while spaces > -1:
            start = spaces
            spaces = text.find(" ", start + 1)
            if spaces - start > 2:
                text = text.replace(text[start:spaces + 1], "-")
            else:
                text = text.replace(text[start:spaces + 1], "_")
    return text

