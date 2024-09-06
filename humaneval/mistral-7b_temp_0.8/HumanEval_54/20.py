

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
    for i in s0:
        char_count.setdefault(i, 0)
        char_count[i] += 1
    for i in s1:
        char_count.setdefault(i, 0)
        char_count[i] += 1
    for i in char_count:
        if char_count[i] % 2 == 1:
            return False
    return True

