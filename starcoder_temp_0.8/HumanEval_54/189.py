

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
    # Check that the two strings are the same length
    if len(s0)!= len(s1):
        return False
    
    # Iterate through each character in s0
    for char in s0:
        # Check if s1 contains the same character
        if char in s1:
            # If so, delete it from s1 so that we don't check it again
            s1 = s1.replace(char, '', 1)
        else:
            # If it doesn't, return False
            return False
    
    # If we've made it this far, the strings must be the same
    return True
