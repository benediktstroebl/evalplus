
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
    # 1. Split string into words and blanks
    words = s.split(' ')
    # 2. Create empty string to hold our shuffled words
    ret = ''
    # 3. Iterate through words, shuffle and append to empty string
    for word in words:
        ret += shuffle(word)
        # 4. If word is not last word, append space to empty string
        if word != words[-1]:
            ret += ' '
    # 5. Return our shuffled string
    return ret
