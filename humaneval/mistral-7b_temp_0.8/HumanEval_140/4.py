
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
    # make a list
    text = list(text)
    # check if the list is empty
    if not text:
        return text
    # check if the index is 0
    if text[0] == " ":
        text[0] = "_"
    # check if the index is not 0
    if text[0] != " ":
        text[0] = text[0]
    # check if the index is greater than 0
    if len(text) > 1:
        if text[0] != " " and text[1] == " ":
            text[1] = "_"
        elif text[0] == " " and text[1] == " ":
            text[1] = "_"
        else:
            text[1] = text[1]
    # check if the index is greater than 1
    if len(text) > 2:
        if text[1] == " " and text[2] != " ":
            text[1] = text[1]
        elif text[1] == " " and text[2] == " ":
