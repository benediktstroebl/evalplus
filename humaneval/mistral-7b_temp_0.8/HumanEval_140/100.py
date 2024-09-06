
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
    new_text = ""
    for i in range(len(text)):
        if i > 0 and i < len(text) - 1:
            if text[i] == " " and text[i - 1] == " " and text[i + 1] == " ":
                new_text += "-"
            else:
                new_text += "_"
        elif i == 0 and text[i + 1] == " ":
            new_text += text[i]
        elif i == len(text) - 1 and text[i - 1] == " ":
            new_text += text[i]
        elif i == len(text) - 1 and text[i - 1] != " ":
            new_text += text[i]
        else:
            new_text += text[i]
    return new_text
