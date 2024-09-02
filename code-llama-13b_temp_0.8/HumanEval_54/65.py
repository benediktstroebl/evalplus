

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
    # This solution is O(n^2), can it be improved?
    # The first string should be the shortest.
    if len(s0) > len(s1):
        s0, s1 = s1, s0
    chars0, chars1 = list(s0), list(s1)
    chars0.sort()
    chars1.sort()
    i, j = 0, 0
    while i < len(chars0) and j < len(chars1):
        if chars0[i] == chars1[j]:
            i += 1
            j += 1
        else:
            if chars0[i] < chars1[j]:
                i += 1
            else:
                j += 1
    return i == len(chars0) and j == len(chars1)

