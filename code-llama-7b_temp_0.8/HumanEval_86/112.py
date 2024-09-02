
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
        return ''
    words = s.split(' ')
    temp_str = ''
    for word in words:
        for letter in word:
            temp_str += letter
    temp_str = temp_str[::-1]
    new_s = ''
    for word in words:
        new_s += temp_str[:len(word)]
        temp_str = temp_str[len(word):]
        new_s += ' '
    return new_s[:-1]

