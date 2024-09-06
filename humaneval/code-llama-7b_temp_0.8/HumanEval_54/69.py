

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

    # 1. A simple linear-time algorithm
    chars = set(s0)
    for c in s1:
        if c not in chars:
            return False
        else:
            chars.remove(c)
    return True

    # 2. A more sophisticated algorithm
    # chars0 = set(s0)
    # chars1 = set(s1)
    # return chars0 == chars1

    # 3. Another more sophisticated algorithm
    # return all(c in s1 for c in s0) and all(c in s0 for c in s1)

