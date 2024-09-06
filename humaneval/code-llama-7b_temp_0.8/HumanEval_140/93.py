
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
    # make a new empty string
    new_string = ''

    # iterate over the given string
    for index, letter in enumerate(text):
        # if the letter is a space
        if letter == ' ':
            # if the index + 1 is greater than the string length, or the next letter is not a space
            if index + 1 >= len(text) or text[index + 1] != ' ':
                # append an underscore
                new_string += '_'
            # if the letter is a space, and the index + 1 is less than the string length, and the next letter is a space
            else:
                # append a hyphen
                new_string += '-'
        # if the letter is not a space
        else:
            # append the letter
            new_string += letter
    # return the new string
    return new_string
