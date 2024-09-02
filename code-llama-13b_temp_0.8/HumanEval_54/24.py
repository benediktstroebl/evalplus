

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

    def build_char_dict(s: str):
        char_dict = {}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        return char_dict

    if len(s0) != len(s1):
        return False

    dict0 = build_char_dict(s0)
    dict1 = build_char_dict(s1)

    for char, val in dict0.items():
        if char not in dict1:
            return False
        if dict1[char] != val:
            return False

    return True

