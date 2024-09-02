

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # check the length of the words
    if len(s0) != len(s1):
        return False
    
    # check if both words have the same number of characters
    if len(s0) != len(set(s0)):
        return False
    
    # check if the characters in the first word are in the same order as in the second word
    for char in set(s1):
        if char not in s0:
            return False
    
    return True