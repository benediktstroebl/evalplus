
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
    if len(text) == 0:
        return ""
    
    # initialize the number of spaces in a row
    spaces_in_a_row = 0
    
    # loop through the text
    for i in range(len(text)):
        # if this is a space, increment the number of spaces
        if text[i] == " ":
            spaces_in_a_row += 1
        # otherwise this is a non-space character
        else:
            # if there are more than 2 spaces in a row, replace all spaces with a dash
            if spaces_in_a_row > 2:
                text = text[:i] + ("-" * spaces_in_a_row) + text[i:]
            # otherwise, replace all spaces with an underscore
            elif spaces_in_a_row > 0:
                text = text[:i] + ("_" * spaces_in_a_row) + text[i:]
            # reset the number of spaces
            spaces_in_a_row = 0
    
    # if there are any spaces at the end of the string, replace them with an underscore
    if spaces_in_a_row > 0:
        text = text + ("_" * spaces_in_a_row)
    
    return text
