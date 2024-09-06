
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
    count_list = [0] * n
    for i in range(n):
        count_list[s[i]] += 1

    i = 0
    while i < n:
        count = count_list[i]
        while count > 0:
            s[i] = chr(ord(s[i]) % len(s))
            count -= 1
        i += 1
    return ''.join(s
