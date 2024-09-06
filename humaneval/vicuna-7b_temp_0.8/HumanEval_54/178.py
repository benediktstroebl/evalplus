

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
    # first, sort the characters in both strings
    char_s0 = sorted(set(s0))
    char_s1 = sorted(set(s1))
    # then, check if all characters in s0 are in char_s1 and vice versa
    return all(char_s0[i] == char_s1[i] for i in range(len(char_s0))) and \
        all(char_s1[i] == char_s0[i] for i in range(len(char_s1)))
