

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
    # count characters
    char_dict0 = {}
    for char in s0:
        if char not in char_dict0:
            char_dict0[char] = 1
        else:
            char_dict0[char] += 1
    char_dict1 = {}
    for char in s1:
        if char not in char_dict1:
            char_dict1[char] = 1
        else:
            char_dict1[char] += 1
    for char in char_dict0:
        if char not in char_dict1:
            return False
        if char_dict0[char] != char_dict1[char]:
            return False
    return True
