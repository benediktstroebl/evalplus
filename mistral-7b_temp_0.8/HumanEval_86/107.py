
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
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s
    else:
        letter = s.split(' ')[0]
        if letter in alphabet:
            arr = list(letter)
            arr.sort()
            letter = ''.join(arr)
        else:
            letter = letter
        return letter + anti_shuffle(s[len(letter)+1:])

