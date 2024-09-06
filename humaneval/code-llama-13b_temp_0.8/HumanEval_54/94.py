

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
    # Exceptions
    if len(s0) != len(s1):
        return False
    if s0 == s1:
        return True
    if set(s0) != set(s1):
        return False

    # Constants
    DECREASE_THRESHOLD = 3

    # Main
    s0_dict = dict()
    s1_dict = dict()
    for char in s0:
        if char in s0_dict:
            s0_dict[char] += 1
        else:
            s0_dict[char] = 1

    for char in s1:
        if char in s1_dict:
            s1_dict[char] += 1
        else:
            s1_dict[char] = 1

    for key in s0_dict:
        s0_dict[key] = abs(s0_dict[key] - s1_dict[key])
        if s0_dict[key] >= DECREASE_THRESHOLD:
            return False

    return True
