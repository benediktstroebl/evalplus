

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
    # should be 0(N)
    # char_count = {}
    # for i in range(len(s0)):
    #     if s0[i] in char_count:
    #         char_count[s0[i]] += 1
    #     else:
    #         char_count[s0[i]] = 1
    # for i in range(len(s1)):
    #     if s1[i] in char_count:
    #         char_count[s1[i]] -= 1
    #         if char_count[s1[i]] == 0:
    #             del char_count[s1[i]]
    #     else:
    #         return False
    # if len(char_count) == 0:
    #     return True
    # else:
    #     return False
    # should be 0(NlogN)
    # sorted_s0 = sorted(s0)
    # sorted_s1 = sorted(s1)
    # if len(sorted_s0) != len(sorted_s1):
    #     return False
    # for i in range(len(s0)):
    #     if sorted_s0[i] != sorted_s1[i]:
    #         return False
    # return True
    # should be 0(2N)
    # char_count0 = {}
    # char_count1 = {}
    # for i in range(len(s0)):
    #     if s0[i] in char_count0:
    #         char_count0[s0[i]] += 1
    #     else:
    #         char_count0[s0[i]] = 1
    #     if s1[i] in char_count1:
    #         char_count1[s1[i]] += 1
    #     else:
    #         char_count1[s1[i]] = 1
    # if len(char_count0) != len(char_count1):
    #     return False
    # for key in char_count0:
    #     if char_count0[key] !=
