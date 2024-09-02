
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
    if text == "":
        return text

    if text[0] == " ":
        text = "_" + text[1:]
    if text[-1] == " ":
        text = text[:-1] + "_"

    new_text = ""
    count = 0
    prev_space = False
    for char in text:
        if char == " ":
            if count == 2:
                new_text += "-"
                prev_space = True
            else:
                new_text += "_"
                count += 1
                prev_space = True
        else:
            new_text += char
            prev_space = False
            count = 0
    return new_text
