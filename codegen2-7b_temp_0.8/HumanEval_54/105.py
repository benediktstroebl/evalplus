

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
    if len(s0)!= len(s1):
        return False
    chars = {}
    for char in s0:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    for char in s1:
        if char in chars:
            if chars[char] == 1:
                chars[char] -= 1
            else:
                chars[char] -= 1
        else:
            return False
    return True
