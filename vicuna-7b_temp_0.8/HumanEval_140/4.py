
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
    # initialize the result string
    result = ""
    # iterate through each character in the text
    for i, c in enumerate(text):
        # check if the character is a space
        if c == " ":
            # replace consecutive spaces with a dash
            if (i+1) < len(text) and text[i+1] == " ":
                result += "-"
                i += 1
            else:
                result += "_"
        # append the character to the result string
        result += c
    return result
