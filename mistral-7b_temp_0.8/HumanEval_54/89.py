

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
    # 1. Check if the words have the same length.
    if len(s0) != len(s1):
        return False

    # 2. Convert each word to a set of its characters.
    s0_set = set(s0)
    s1_set = set(s1)

    # 3. Check if the sets have the same elements.
    if s0_set == s1_set:
        return True
    else:
        return False

