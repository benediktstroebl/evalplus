

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

    if len(s0)!= len(s1):
        return False
    count = [0]*26
    for i in range(len(s0)):
        count[ord(s0[i]) - ord('a')] += 1
        count[ord(s1[i]) - ord('a')] -= 1
    for i in range(len(count)):
        if count[i]!= 0:
            return False
    return True
