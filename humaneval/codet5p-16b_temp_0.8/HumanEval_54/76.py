

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

    s0_counter = dict()
    for char in s0:
        if char in s0_counter:
            s0_counter[char] += 1
        else:
            s0_counter[char] = 1

    for char in s1:
        if char in s0_counter and s0_counter[char] > 0:
            s0_counter[char] -= 1
        else:
            return False

    return True

