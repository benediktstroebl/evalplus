

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
    # Count the number of each character in both strings.
    # Make sure we use 0 for a character that was not found,
    # so the comparison doesn't throw an error later.
    s0_counts = {}
    s1_counts = {}
    for s in s0:
        s0_counts[s] = s0_counts.get(s, 0) + 1
    for s in s1:
        s1_counts[s] = s1_counts.get(s, 0) + 1

    # Check if they have the same number of each character.
    return s0_counts == s1_counts

