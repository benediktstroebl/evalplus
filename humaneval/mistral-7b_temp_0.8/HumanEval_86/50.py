
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
    s = list(s)
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue
        j = 0
        while j < len(s) - 1:
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
            j += 1
        i += 1
    s = ''.join(s)
    return s
