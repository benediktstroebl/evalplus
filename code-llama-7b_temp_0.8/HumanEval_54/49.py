

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
    chars = 'abcdefghijklmnopqrstuvwxyz'
    s0_char_count = {char: 0 for char in chars}
    s1_char_count = {char: 0 for char in chars}

    for char in s0:
        s0_char_count[char] += 1

    for char in s1:
        s1_char_count[char] += 1

    for char, count in s0_char_count.items():
        if count != s1_char_count[char]:
            return False

    return True
