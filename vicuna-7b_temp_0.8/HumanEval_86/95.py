
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
    # check if string is not empty
    if len(s) == 0:
        return ""
    
    # split the string on whitespace
    words = s.split()
    
    # reverse the order of characters in each word
    for i in range(len(words[0])):
        words[0], words[1] = words[1], words[0]
    
    # join the words back into a string
    return ''.join(words)