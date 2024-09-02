

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
    # Create two sets to store the characters of s0 and s1
    s0_set = set(s0)
    s1_set = set(s1)

    # Add each character to the set of both words and remove it from the original string
    s0_set.update(s0)
    s1_set.update(s1)
    s0_set.pop()
    s1_set.pop()

    # Check if the sets of characters are equal
    return s0_set == s1_set
