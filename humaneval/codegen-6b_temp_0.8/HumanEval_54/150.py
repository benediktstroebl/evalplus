

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
    for i in range(len(s0)):
        if s0[i] in chars:
            chars[s0[i]].append(i)
        else:
            chars[s0[i]] = [i]
    for i in range(len(s1)):
        if s1[i] in chars:
            if chars[s1[i]] == i:
                return True
            else:
                return False
        else:
            return False
    return True
