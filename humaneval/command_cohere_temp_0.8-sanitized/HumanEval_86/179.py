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
    # Iterate over each word and sort each word separately
    result = ' '.join(char_sorted(word) for word in s.split(' '))
    
    # If the input string ends with a space, we need to add it to the end of the result
    if s.endswith(' '):
        result += ' '
    
    return result
def char_sorted(word):
    """
    Sort characters in word from smallest to largest
    """
    return ''.join(sorted(word))