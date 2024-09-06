
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
    start = 0
    end = 1
    while end < len(s):
        if s[start] == ' ' or s[end] == ' ':
            end += 1
            continue
        elif ord(s[start]) > ord(s[end]):
            s[start], s[end] = s[end], s[start]
        start += 1
        end += 1
    return ''.join(s)

