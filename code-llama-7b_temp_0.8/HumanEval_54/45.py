

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
    # SOLUTION: Use a dictionary to record the number of each character in s0, then compare s1.
    # If s1 is the same chars, all the chars in s1 should be equal to or less than the number of chars in s0.
    # e.g. s1 = 'abcd', s0 = 'dddddddabc'.
    # After using s0 to record the number of each chars, {'d': 7, 'a': 1, 'b': 1, 'c': 1}.
    # Then s1 is same chars with s0 if 'a' <= 7, 'b' <= 7, 'c' <= 7, and 'd' <= 7.
    # So 'abcd' is same chars with 'dddddddabc', but not 'dddddddabce'.
    # The same logic applies to the other examples.
    cnt = {}
    for ch in s0:
        if ch in cnt:
            cnt[ch] += 1
        else:
            cnt[ch] = 1
    for ch in s1:
        if ch in cnt:
            cnt[ch] -= 1
            if cnt[ch] < 0:
                return False
        else:
            return False
    return True

