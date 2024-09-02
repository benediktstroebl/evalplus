
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
    # initialize the new string
    new_string = ""
    
    # iterate through the characters in the text
    for char in text:
        # check if the character is a space
        if char == " ":
            # if the string has more than 2 consecutive spaces
            if (new_string[-2] == " " and new_string[-1] == " ") or (new_string[-1] == " " and new_string[-2] == " "):
                # replace the spaces with -
                new_string += "-"
            # if the current space is the first character in the string
            elif new_string == "":
                # replace the space with an underscore
                new_string += "_"
            # replace all other spaces with an underscore
            else:
                new_string += "_"
        # if the character is not a space
        else:
            new_string += char
    
    return new_string
