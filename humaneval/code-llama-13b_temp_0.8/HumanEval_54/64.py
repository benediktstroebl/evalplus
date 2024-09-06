

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
    if len(s0) != len(s1):
        return False
    # create a copy of the first string
    s0_copy = s0
    for c in s0:
        if c in s1:
            # found the character, delete it from the copy
            s0_copy = s0_copy.replace(c, '', 1)
        else:
            # the character is not in the second string
            return False
    # if we got here, we found all the characters in the second string
    return True

