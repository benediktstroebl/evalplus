

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

    # make a list of the characters of the first string
    string_0 = list(s0)
    # make a list of the characters of the second string
    string_1 = list(s1)

    # loop over the characters of the first string
    for char_0 in string_0:
        # loop over the characters of the second string
        for char_1 in string_1:
            # check if the characters are the same
            if char_0 == char_1:
                # if the characters are the same, remove them from both strings
                string_0.remove(char_0)
                string_1.remove(char_1)
                # print(string_0)
                # print(string_1)
                # check if the characters are the same
                if len(string_0) == 0 and len(string_1) == 0:
                    return True
                break
            else:
                continue

    return False

