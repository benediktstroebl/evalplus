
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

    # split string by space
    # create empty list
    # for each word in string
    # sort letters in word
    # add word to list
    # join list by space

    # 1st way
    def ascii_sort(word):
        return ''.join(sorted(word))

    # 2nd way
    def ascii_sort(word):
        return ''.join(sorted(word, key = ord))

    def anti_shuffle(s):
        return ' '.join([ascii_sort(word) for word in s.split()])

    # 3rd way
    def anti_shuffle(s):
        return ' '.join(sorted(s.split(), key=lambda x: ''.join(sorted(x))))
