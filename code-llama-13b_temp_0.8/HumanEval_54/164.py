

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
    s0_dict = {}
    for letter in s0:
        if letter not in s0_dict:
            s0_dict[letter] = 1
        else:
            s0_dict[letter] += 1
    for letter in s1:
        if letter in s0_dict and s0_dict[letter] > 0:
            s0_dict[letter] -= 1
        else:
            return False
    return True

