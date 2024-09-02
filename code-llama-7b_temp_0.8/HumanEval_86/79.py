
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

    # approach: replace each word with its shuffled version and
    # then reassemble the words in their original order
    #
    # first, separate the string by spaces into a list of words
    # then shuffle each word, and reassemble into a string
    # finally return the string
    # O(n) time, O(n) space, n = number of chars in the string
    #
    # assume the input string is valid, i.e. only spaces and letters
    # and no blank strings

    # case where string only contains spaces
    if s == ' ':
        return s

    # replace each word with its shuffled version
    words = s.split(' ')
    words_shuffled = []
    for word in words:
        word_shuffled = shuffle_word(word)
        words_shuffled.append(word_shuffled)

    # reassemble into a string
    s_shuffled = ' '.join(words_shuffled)

    return s_shuffled

