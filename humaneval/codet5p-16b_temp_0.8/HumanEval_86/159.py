
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

    if s == '':
        return s
    l = s.split()
    new_s = ''
    for i in range(0, len(l)):
        s = ''
        for c in l[i]:
            s += chr(ord(c))
        new_s += s
        if i < len(l)-1:
            new_s +=''
    return new_s
