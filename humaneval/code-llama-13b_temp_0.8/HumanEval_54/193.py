

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
    # Hint: Try making a list of 26 booleans (one for each letter of the alphabet), initialized to False.
    # Use it to keep track of which letters you've seen in each string.
    # ... or use a dict of chars -> bool
    if len(s0) != len(s1):
        return False
    if len(s0) == 0 and len(s1) == 0:
        return True

    s0_bools = {}
    s1_bools = {}
    for c in s0:
        if c not in s0_bools:
            s0_bools[c] = True
    for c in s1:
        if c not in s1_bools:
            s1_bools[c] = True
    
    for char, bool1 in s0_bools.items():
        if char in s1_bools:
            if bool1 != s1_bools[char]:
                return False
        else:
            return False
    return True

