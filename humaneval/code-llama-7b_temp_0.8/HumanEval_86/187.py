
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

    # remove all leading and trailing spaces
    s = s.strip()
    # split the sentence into a list of words
    words = s.split()
    # store the length of the list
    length = len(words)

    # create an empty string
    string = ''

    # loop through the words and the length
    for i in range(length):
        # get the character list from each word
        chars = list(words[i])
        # sort the character list in ascending order
        chars.sort()
        # add the character list to the string variable
        string += "".join(chars)
        # add a space to the string variable
        string += ' '

    # return the string
    return string

