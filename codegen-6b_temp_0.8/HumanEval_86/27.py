
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
    
    new_s = ''.join(sorted(s))
    return new_s
    

"""
    Given a string, find the length of the longest substring without repeating characters.
    
    Examples:
    Longest substring without repeating characters for "abcabcbb" is "abc" which the length is 3
    Longest substring without repeating characters for "bbbbb" is "b" which the length is 1
    Longest substring without repeating characters for "pwwkew" is "wke" which the length is 3
"""
