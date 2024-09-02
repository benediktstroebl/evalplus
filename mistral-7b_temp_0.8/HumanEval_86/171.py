
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
    n = len(s)
    new_s = []
    i = 0
    while i < n:
        c = s[i]
        if c.isspace():
            new_s.append(c)
            i += 1
        else:
            new_s.append(''.join(sorted(list(s[i]))))
            i += 1
    return ''.join(new_s)
