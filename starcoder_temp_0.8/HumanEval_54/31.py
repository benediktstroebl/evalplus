

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
    # Hint: https://docs.python.org/3/library/stdtypes.html#set
    # Hints:
    #   * Use set to remove duplicates
    #   * Use sorted to sort the strings
    #   * Use a for loop to check every letter
    #   * Use the == operator to compare the length
    #   * Use a return statement to return the final result
    s0 = set(sorted(s0))
    s1 = set(sorted(s1))
    if len(s0) == len(s1):
        for i in s0:
            if i in s1:
                pass
            else:
                return False
        return True
    else:
        return False
