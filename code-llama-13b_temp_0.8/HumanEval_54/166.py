

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
    counter = dict()
    for char in s0:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    for char in s1:
        if char in counter:
            counter[char] -= 1
        else:
            return False
    return all(value == 0 for value in counter.values())
