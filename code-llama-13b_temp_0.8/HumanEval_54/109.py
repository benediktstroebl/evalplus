

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
    # make sure s0 is the shorter of the two strings
    if len(s0) > len(s1):
        s0, s1 = s1, s0
    count0 = Counter(s0)
    count1 = Counter(s1)
    for char0, count0 in count0.items():
        if char0 not in count1 or count1[char0] < count0:
            return False
    return True

