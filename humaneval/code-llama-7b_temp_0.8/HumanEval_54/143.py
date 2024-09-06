

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

    chars_0 = {}
    chars_1 = {}

    for char in s0:
        chars_0[char] = True

    for char in s1:
        chars_1[char] = True

    for char in chars_0:
        if char not in chars_1:
            return False

    for char in chars_1:
        if char not in chars_0:
            return False

    return True

