

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

    char_count = {}
    for c in s0:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    for c in s1:
        if c not in char_count:
            return False
        else:
            char_count[c] -= 1
            if char_count[c] == 0:
                del char_count[c]
    return len(char_count) == 0

