

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
    return set(s0) == set(s1)


assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
assert same_chars('abcd', 'dddddddabc')
assert same_chars('dddddddabc', 'abcd')
assert same_chars('eabcd', 'dddddddabc')
assert not same_chars('abcd', 'dddddddabce')
assert not same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
