

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
    # check if the length of the two words is the same
    if len(s0) != len(s1):
        return False
    # check if the first character is the same
    if s0[0] != s1[0]:
        return False
    # check if the first character is not a letter
    if not s0[0].isalpha() and s0[0].isupper() != s1[0].isupper():
        return False
    # check if all the characters after the first character are the same
    return all(c in s1[1:].lower() for c in s0[1:].lower())