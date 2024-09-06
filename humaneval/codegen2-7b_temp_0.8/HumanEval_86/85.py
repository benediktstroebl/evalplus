
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
    s = s.split(' ')
    for i in range(0,len(s)):
        for j in range(len(s[i])-1):
            if ord(s[i][j]) > ord(s[i][j+1]):
                t = s[i][j]
                s[i][j] = s[i][j+1]
                s[i][j+1] = t
    return''.join(
