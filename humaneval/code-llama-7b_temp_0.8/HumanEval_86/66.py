
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
    # creat a blank list to store the words
    words = []
    # separate the word with a space
    s = s.split()
    # iterate through the word list and sort each word
    for word in s:
        word = ''.join(sorted(word))
        # add the word to the words list
        words.append(word)
    # add the blank spaces
    words = " ".join(words)
    return words
