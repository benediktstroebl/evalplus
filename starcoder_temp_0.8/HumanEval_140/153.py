
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
    # replace all spaces with underscores
    # and find all the positions of the spaces
    spaces = [pos for pos, char in enumerate(text) if char =='']
    # create a new text
    new_text = []
    # iterate over all characters in the text
    for i, char in enumerate(text):
        # if the character is a space, 
        # replace it with an underscore
        if char =='':
            new_text.append('_')
        # if the character is not a space
        else:
            # if the position of the character is in the list of spaces, 
            # add a dash to the new text
            if i in spaces:
                new_text.append('-')
            # else just add the character to the new text
            else:
                new_text.append(char)
    # join the characters in the new text and return the result
    return ''.join(new_text)
