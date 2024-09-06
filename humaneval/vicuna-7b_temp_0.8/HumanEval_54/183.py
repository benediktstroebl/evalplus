

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
    # initialize two sets, one for s0 and one for s1
    set0 = set()
    set1 = set()
    
    # iterate over the characters in s0
    for char in s0:
        set0.add(char)
        
    # add all the characters in s1 to the set of s0
    for char in s1:
        set0.add(char)
    
    # check if set0 contains all the characters in set1
    return set0 == set1