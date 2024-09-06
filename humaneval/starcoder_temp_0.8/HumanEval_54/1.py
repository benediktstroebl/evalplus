

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

    assert isinstance(s0, str), f"s0 must be a string, got {s0}"
    assert isinstance(s1, str), f"s1 must be a string, got {s1}"

    # In general:
    #for c in s1:
    #    if c not in s0:
    #        return False
    #return True

    # More efficient:
    return set(s0) == set(s1)

