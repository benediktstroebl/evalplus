

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
    # Convert both strings to a list of characters
    char_list0 = set(s0)
    char_list1 = set(s1)

    # Compare the length of the two lists
    if len(char_list0) != len(char_list1):
        return False

    # Compare each character in turn
    for i, ch0 in enumerate(char_list0):
        if ch0 != char_list1[i]:
            return False

    return True
