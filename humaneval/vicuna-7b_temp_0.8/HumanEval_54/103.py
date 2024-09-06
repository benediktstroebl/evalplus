

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
    # count the number of characters in each string
    n0 = len(s0)
    n1 = len(s1)
    # count the number of characters in the union of the two strings
    n = max(n0, n1)
    # use a dictionary to count the frequency of each character in the two strings
    d = {ord(char): 0 for char in s0 + s1}
    # iterate over the characters in the dictionary, counting the number of times each character appears in both strings
    for char in d:
        n -= d[char]
        if (ord(s0[n//2]) == char and ord(s1[n//2]) == char or
            ord(s0[n//2]) == ord(char) + 95 and ord(s1[n//2]) == ord(char) + 95):
            d[char] += 1
    return n == 0