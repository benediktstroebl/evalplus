
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
    print('----------------------------------------')
    # init empty list to store fixed strings
    fixed_text = []
    # split string by spaces to get list of words
    for word in text.split():
        # first, count how many spaces are in this word
        spaces = 0
        for char in word:
            if char == ' ':
                spaces += 1
        # if there are no spaces, append the word to the list
        if spaces == 0:
            fixed_text.append(word)
        # otherwise, replace spaces with underscores
        else:
            word = word.replace(' ','_')
            # if word is longer than 2, then replace multiple spaces with -
            if len(word) > 2:
                word = word.replace('__','-')
            # append the fixed word to the list
            fixed_text.append(word)
    # join the list items with a single space and return the result
    return ' '.join(fixed_text)
