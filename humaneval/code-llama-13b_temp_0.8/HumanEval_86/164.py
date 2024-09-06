
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

    # 1) split the string into words
    # 2) for each word, sort the characters and reconstruct the word
    # 3) reconstruct the string

    def _sorted_str(s):
        return ''.join(sorted(s))

    words = s.split(' ')
    return ' '.join([_sorted_str(word) for word in words])

