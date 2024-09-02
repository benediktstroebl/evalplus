

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

    # s0_counter = {}
    # for letter in s0:
    #     if letter in s0_counter:
    #         s0_counter[letter] += 1
    #     else:
    #         s0_counter[letter] = 1

    # s1_counter = {}
    # for letter in s1:
    #     if letter in s1_counter:
    #         s1_counter[letter] += 1
    #     else:
    #         s1_counter[letter] = 1

    # for key in s0_counter.keys():
    #     if key not in s1_counter or s0_counter[key] != s1_counter[key]:
    #         return False
    # return True

    s0_counter = collections.Counter(s0)
    s1_counter = collections.Counter(s1)
    return s0_counter == s1_counter
