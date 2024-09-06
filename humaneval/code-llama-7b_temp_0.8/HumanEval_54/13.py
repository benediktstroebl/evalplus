

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
    if not (len(s0) and len(s1)):
        return False
    char_count = {}
    for ch in s0:
        char_count[ch] = char_count.get(ch, 0) + 1

    for ch in s1:
        if ch not in char_count or char_count[ch] == 0:
            return False
        else:
            char_count[ch] -= 1

    return True

