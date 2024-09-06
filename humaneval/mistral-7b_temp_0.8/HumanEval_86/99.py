
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
    import string
    charset = string.ascii_letters + string.punctuation + " "
    charset_set = set(charset)

    def char_ord(ch):
        try:
            return charset_set.index(ch)
        except ValueError:
            return -1

    def ascii_ord(word):
        return ''.join(sorted(word, key=char_ord))

    return ' '.join([ascii_ord(w) for w in s.split()])

