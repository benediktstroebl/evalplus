

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
    # Count the characters
    # If the counts are the same, then the characters are the same
    # Else, the characters are different
    count_chars0 = {}
    count_chars1 = {}

    for char in s0:
        if char in count_chars0:
            count_chars0[char] += 1
        else:
            count_chars0[char] = 1

    for char in s1:
        if char in count_chars1:
            count_chars1[char] += 1
        else:
            count_chars1[char] = 1

    if count_chars0 == count_chars1:
        return True
    else:
        return False

