
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

    # find the indices of all the spaces
    indices = [i for i, char in enumerate(text) if char == " "]
    # loop through the indices and replace the text at those indices
    # for multiple spaces
    for i in indices:
        if i + 1 in indices and i + 2 in indices:
            text = text[:i] + "-" + text[i + 1 :]
    # replace the text at the remaining indices
    for i in indices:
        text = text[:i] + "_" + text[i + 1 :]
    return text

