

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
    # 1. convert both words to lower case
    s0 = s0.lower()
    s1 = s1.lower()
    # 2. split both words into a list of characters
    s0_chars = s0.split()
    s1_chars = s1.split()
    # 3. compare the two lists of characters
    return s0_chars == s1_chars
