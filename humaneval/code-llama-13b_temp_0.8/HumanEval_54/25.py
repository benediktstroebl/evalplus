

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
    chars = set()
    for char in s0:
        if char in chars:
            chars.discard(char)
        else:
            chars.add(char)

    for char in s1:
        if char in chars:
            chars.discard(char)
        else:
            chars.add(char)

    return len(chars) == 0

