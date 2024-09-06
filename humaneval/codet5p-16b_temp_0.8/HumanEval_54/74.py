

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
    char_map = [0] * 256
    for char in s0:
        char_map[ord(char)] += 1
    for char in s1:
        char_map[ord(char)] -= 1
        if char_map[ord(char)] < 0:
            return False
    return True
