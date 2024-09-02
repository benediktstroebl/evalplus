

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
    if s0 == '' or s1 == '':
        return False

    # Algorithm
    c0 = s0[0]
    c1 = s1[0]

    while True:
        i0 = s0.find(c0)
        i1 = s1.find(c1)

        if i0 == -1:
            return False
        else:
            s0 = s0[:i0] + s0[i0+1:]

        if i1 == -1:
            return False
        else:
            s1 = s1[:i1] + s1[i1+1:]

        if s0 == '' or s1 == '':
            return False

        c0 = s0[0]
        c1 = s1[0]

    return True

