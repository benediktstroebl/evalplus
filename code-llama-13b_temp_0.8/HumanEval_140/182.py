
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

    # keep track of how many spaces we are looking at
    space_count = 0

    # iterate through the text
    for char in text:
        # if we find a space...
        if char == " ":
            # if this is the first space we have seen...
            if space_count == 0:
                # replace it with an underscore
                text = text.replace(" ","_",1)
            # if we have seen a space before...
            else:
                # replace it with a dash
                text = text.replace(" ","-",1)
            # increment our counter
            space_count += 1
        else:
            # if we have seen more than 1 spaces...
            if space_count > 1:
                # replace all the spaces we saw before with dashes
                text = text.replace(" ","-",space_count)
            # reset our space counter
            space_count = 0

    return text
