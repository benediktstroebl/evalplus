

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
    # use a dictionary to count the characters in s1 and s0
    char_counts = {}
    for c in s1:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    for c in s0:
        if c in char_counts:
            if char_counts[c] != 1:
                return False
    return True