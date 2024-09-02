
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
    chars = sorted(set(s))
    str = ''.join(chars)
    space_count = 0
    for i, c in enumerate(s):
        if c =='':
            space_count += 1
        else:
            str = str[:i-space_count] + chr(ord(c)+1) + str[i+1:]
            space_count = 0
    return
