

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
    # Ensure s1 is shorter
    if len(s0) > len(s1):
        s0, s1 = s1, s0

    # Check if each character in s0 is in s1
    for i in range(len(s0)):
        if s0[i] not in s1:
            return False

    # Check if all characters in s1 are in s0
    return not (len(set(s1)) > len(set(s0)))
