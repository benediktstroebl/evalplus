

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
    # Create a set of characters for each word
    set0 = set(s0)
    set1 = set(s1)

    # Check if the sets have the same number of elements
    if len(set0) != len(set1):
        return False

    # Check if all elements in one set are also in the other set
    for element in set0:
        if element not in set1:
            return False

    return True