

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
    # Make dictionaries from both strings
    s0_dict = {c: s0.count(c) for c in s0}
    s1_dict = {c: s1.count(c) for c in s1}
    # Check the keys and values
    for k, v in s0_dict.items():
        if k not in s1_dict.keys() or s1_dict[k] != v:
            return False
    return True

