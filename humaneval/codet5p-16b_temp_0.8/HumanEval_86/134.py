
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

    s = s.split()
    s_ord = []
    for word in s:
        w_ord = []
        for c in word:
            w_ord.append(ord(c))
        w_ord.sort()
        s_ord.append(''.join([chr(c) for c in w_ord]))
    return''.join(s_ord)
