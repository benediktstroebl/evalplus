
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

    # replace the spaces with underscores 
    text = text.replace(" ", "_")

    # iterate through each character and check if the previous character was also a space 
    # if it is, then replace it with a dash
    new_text = ""
    for i in range(len(text)-1):
        if text[i] == "_" and text[i+1] == "_":
            new_text += "-"
        else:
            new_text += text[i]
    # add the last character if it's not a space
    if text[-1] != "_":
        new_text += text[-1]
    
    # return the new text
    return new_text
