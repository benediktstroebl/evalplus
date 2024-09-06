
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
    # initialize counter for consecutive spaces
    spaces = 0
    # initialize empty string to store the results
    new_text = ""
    # loop through the text
    for c in text:
        # if c is a space
        if c == " ":
            # increment spaces counter by 1
            spaces += 1
        # if c is not a space
        else:
            # if spaces is greater than 1
            if spaces > 1:
                # replace spaces with a -
                new_text += "-"
            # otherwise
            else:
                # replace spaces with an underscore
                new_text += "_"
            # reset spaces to 0
            spaces = 0
        # if c is a space
        if c == " ":
            # append the character to the new text
            new_text += c
    # if spaces is greater than 1
    if spaces > 1:
        # replace spaces with a -
        new_text += "-"
    # otherwise
    else:
        # replace spaces with an underscore
        new_text += "_"
    # return the new text
    return new_text
