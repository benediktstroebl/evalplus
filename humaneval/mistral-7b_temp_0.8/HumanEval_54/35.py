

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
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')

    if s1 == s2:
        return True
    elif len(s1) != len(s2):
        return False
    else:
        for char in s1:
            if char in s2:
                s2 = s2.replace(char, '')
            else:
                return False
        return True
