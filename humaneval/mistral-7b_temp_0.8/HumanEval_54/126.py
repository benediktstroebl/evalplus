

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

    def char_count(word: str):
        """Count number of occurrences of characters in word.
        >>> char_count('aabcccde')
        {'a': 2, 'b': 1, 'c': 3, 'd': 1, 'e': 1}
        """
        counts = {}
        for c in word:
            counts[c] = counts.get(c, 0) + 1
        return counts

    counts0 = char_count(s0)
    counts1 = char_count(s1)
    return counts0 == counts1

