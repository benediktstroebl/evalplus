

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
    if len(s0) != len(s1):
        return False

    # counter for number of letters
    count = {}
    for letter in s0:
        count[letter] = count.get(letter, 0) + 1

    for letter in s1:
        if letter in count:
            count[letter] -= 1
            if count[letter] == 0:
                del count[letter]
        else:
            return False
    return len(count) == 0

