

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

    # We can use dictionary to solve this problem easily.
    # Loop through the s0 and count the characters.
    s0_dict = {}
    for char in s0:
        if char not in s0_dict:
            s0_dict[char] = 1
        else:
            s0_dict[char] += 1

    # Loop through the s1 and check if the characters exist in s0
    # If it exists, decrease the count of that character.
    for char in s1:
        if char in s0_dict and s0_dict[char] > 0:
            s0_dict[char] -= 1
        else:
            return False

    return True

