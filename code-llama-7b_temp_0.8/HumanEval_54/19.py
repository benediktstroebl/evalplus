

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

    # Get letters from the two strings
    l0 = [char for char in s0]
    l1 = [char for char in s1]
    # Check if they are the same size
    if len(l0) != len(l1):
        return False
    # Check if all letters are the same
    for i, char in enumerate(l0):
        if char != l1[i]:
            return False
    return True

