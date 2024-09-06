

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

    # get the list of letters from the first word
    letters0 = list(s0)
    # remove duplicate letters from that list
    letters0 = list(dict.fromkeys(letters0))

    # get the list of letters from the second word
    letters1 = list(s1)
    # remove duplicate letters from that list
    letters1 = list(dict.fromkeys(letters1))

    # return the result of comparing the two lists
    return letters0 == letters1

