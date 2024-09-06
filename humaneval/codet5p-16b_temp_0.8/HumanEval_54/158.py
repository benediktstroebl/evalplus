

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

    chars_count = dict()
    for char in s0:
        if char not in chars_count:
            chars_count[char] = 1
        else:
            chars_count[char] += 1

    for char in s1:
        if char not in chars_count:
            return False
        else:
            if chars_count[char] == 0:
                return False
            else:
                chars_count[char] -= 1

    return all(chars_count[char] == 0 for char in chars_count)
