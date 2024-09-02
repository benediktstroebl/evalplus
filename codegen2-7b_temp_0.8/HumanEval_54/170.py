

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
    def count_chars(s):
        """
        Return a list of characters and their frequency.
        """
        count_dict = {}
        for char in s:
            count_dict[char] = count_dict.get(char, 0) + 1
        return count_dict
    count0 = count_chars(s0)
    count1 = count_chars(s1)
    if count0 == count1:
        return True
    else:
        return False

