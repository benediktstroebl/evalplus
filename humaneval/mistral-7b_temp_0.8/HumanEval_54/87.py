

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
    if len(s0) != len(s1):
        return False
    chars = {}
    for i in s0:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    for i in s1:
        if i not in chars:
            return False
        else:
            chars[i] -= 1
            if chars[i] < 0:
                return False
    return True

