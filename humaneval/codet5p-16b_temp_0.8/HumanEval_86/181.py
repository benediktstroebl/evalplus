
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

    if len(s) <= 1:
        return s

    s = s.split()
    new_s = []
    sorted_s = []
    for i in s:
        new_s = sorted(i, key=lambda x: ord(x))
        new_s = ''.join(new_s)
        sorted_s.append(new_s)
    s =''.join(sorted_s)
    return s
