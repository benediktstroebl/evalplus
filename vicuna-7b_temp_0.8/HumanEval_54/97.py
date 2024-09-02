

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
    # Convert the words to lists of characters
    words0 = list(map(lambda x: x.lower(), s0.split()))
    words1 = list(map(lambda x: x.lower(), s1.split()))

    # Compare the lists element by element
    for i in range(len(words0)):
        if words0[i] != words1[i]:
            return False
    return True
