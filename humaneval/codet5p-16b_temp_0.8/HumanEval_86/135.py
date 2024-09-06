
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
    out = []
    for i in range(len(s)):
        temp = [0 for _ in range(len(s[i]))]
        for j in range(len(s[i])):
            temp[j] = ord(s[i][j])
        temp.sort()
        out.append(''.join([chr(n) for n in temp]))
    return''.join(out)
