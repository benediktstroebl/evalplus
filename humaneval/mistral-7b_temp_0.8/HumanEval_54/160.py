

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
    # Check if both strings have the same length.
    if len(s0) != len(s1):
        return False
    # Iterate over every character and check if it is present in both strings.
    for char in s0:
        # If the character is not present in the other string, return False.
        if char not in s1:
            return False
    # If all characters are present in both strings, return True.
    return True
