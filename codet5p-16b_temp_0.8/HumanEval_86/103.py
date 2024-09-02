
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    # split string by spaces
    words = s.split()
    # create empty string
    new_string = ''
    # iterate over words
    for word in words:
        # create empty string
        new_word = ''
        # iterate over each character in word
        for char in word:
            # append character to new word
            new_word += char
        # sort string
        new_word = sorted(new_word)
        # add word to new string
        new_string += new_word
    # append space between words
    new_string +=''
    # return new string
    return new_string
