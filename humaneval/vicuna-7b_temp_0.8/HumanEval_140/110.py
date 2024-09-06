
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
    # split the string into a list of words
    words = text.split()

    # initialize an empty list to store the replaced words
    replacement_list = []

    # loop through the words
    for word in words:
        # check if the word contains 2 or more consecutive spaces
        if ' ' in word and len(word) >= 3:
            # replace all consecutive spaces in the word with -
            word = word.replace(' ', '-')
        else:
            # replace all spaces in the word with underscores
            word = word.replace(' ', '_')

        # add the word to the replacement list
        replacement_list.append(word)

    # join the replaced words in the list with underscores
    return '_'.join(replacement_list)
