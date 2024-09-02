

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

    # make sure the string lengths are the same
    if len(s0) != len(s1):
        return False

    # create a counter for each string
    count_s0 = dict()
    count_s1 = dict()

    # iterate through string 1 and count the characters
    for char in s0:
        if char not in count_s0:
            count_s0[char] = 0
        count_s0[char] += 1

    # iterate through string 2 and count the characters
    for char in s1:
        if char not in count_s1:
            count_s1[char] = 0
        count_s1[char] += 1

    # check if the counters are the same for each character
    for key, value in count_s0.items():
        if key not in count_s1 or value != count_s1[key]:
            return False

    return True

