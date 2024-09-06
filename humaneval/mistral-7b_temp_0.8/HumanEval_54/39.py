

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
    # Convert both strings to lowercase
    s0 = s0.lower()
    s1 = s1.lower()

    # Sort each string
    s0 = ''.join(sorted(s0))
    s1 = ''.join(sorted(s1))

    # Check if the sorted strings are the same
    return s0 == s1
