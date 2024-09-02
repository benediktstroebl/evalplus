
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

    # replace all single spaces with underscores
    text = text.replace(" ", "_")

    # create an array of all spaces in the string
    spaces = [index for index, char in enumerate(text) if char == " "]

    # check for two consecutive spaces and replace with -
    if len(spaces) > 1:
        spaces = [index for index, char in enumerate(text) if char == " "]
        for index in range(len(spaces) - 1):
            text = text[:spaces[index]] + "-" + text[spaces[index + 1]:]

    return text
