
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
    if len(s) == 0:
        return s
    elif s == '':
        return s
    elif len(s) == 1:
        return s
    elif s == None:
        return s
    else:
        words = s.split()
        return ' '.join(map(lambda word: ''.join(sorted(word)), words))
