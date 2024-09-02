

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

    s0_chars_list = list(s0)
    s1_chars_list = list(s1)
    if len(s0_chars_list)!= len(s1_chars_list):
        return False
    
    for s0_chr in s0_chars_list:
        if s0_chr in s1_chars_list:
            s1_chars_list.remove(s0_chr)
        else:
            return False
    
    return True

