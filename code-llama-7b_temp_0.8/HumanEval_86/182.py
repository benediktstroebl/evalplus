
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
    # separate the sentence in words
    # sort each word
    # return the sentence ordered

    # check for empty sentece
    if s == '':
        return s

    # split the sentence in words
    words = s.split()

    # sort the words
    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))

    # return the sorted sentence
    return ' '.join(words)

