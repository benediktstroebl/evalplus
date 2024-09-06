

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
    chars_dict = {}
    for char in s0:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    for char in s1:
        if char not in chars_dict:
            return False
        chars_dict[char] -= 1
    for value in chars_dict.values():
        if value!= 0:
            return False
    return True
