
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
    # split text into a list of words
    words = text.split()
    # initialize a list to store the result
    result = []
    # iterate over the words
    for word in words:
        # check if the word has only one space
        if len(word) == 1 and ' ' in word:
            # if the word has more than one space, 
            # replace all consecutive spaces with -
            result.append(word.replace(' '.join(words), '-'))
        else:
            # if the word has only one space, 
            # replace all spaces with underscores
            result.append(word.replace(' '.join(words), '_'))
    # join the result back to a string
    return ' '.join(result)
