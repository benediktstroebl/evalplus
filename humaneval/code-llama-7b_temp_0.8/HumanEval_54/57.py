

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
    # if s0 is empty
    if len(s0) == 0:
        # then s1 must be empty as well
        return len(s1) == 0

    # if s1 is empty
    if len(s1) == 0:
        # then s0 must be empty as well
        return len(s0) == 0

    # initialize a flag
    flag = True

    # check if both strings have the same length
    if len(s0) != len(s1):
        # set the flag to false
        flag = False

    # if the flag is true
    if flag:
        # loop over the string
        for i in range(0, len(s0)):
            # if the character at index i is not the same as the
            # character at index i in the other string
            if s0[i] != s1[i]:
                # set the flag to false
                flag = False

    return flag


