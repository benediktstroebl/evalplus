
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
    s_lower = s.lower()
    s_shuffled = ''
    for c in s_lower:
        if c.isalpha():
            c_value = ord(c)
            c_value += c_value
            s_shuffled += chr(c_value)
        else:
            s_shuffled += c
    return s_shuffled