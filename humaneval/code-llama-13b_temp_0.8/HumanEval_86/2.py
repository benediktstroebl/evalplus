
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

    def get_word(s):
        while not s.isalpha() and s != '':
            s = s[1:]
        word = s
        while s.isalpha() and s != '':
            s = s[1:]
        return (word, s)

    if s == '':
        return ''
    else:
        word, s = get_word(s)
        word = ''.join(sorted(word))
        return word + ' ' + anti_shuffle(s)

