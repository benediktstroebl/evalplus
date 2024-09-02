

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

    def check_chars(s0, s1):
        chars_s0 = {}
        chars_s1 = {}
        for char in s0:
            if char in chars_s0:
                chars_s0[char] += 1
            else:
                chars_s0[char] = 1

        for char in s1:
            if char in chars_s1:
                chars_s1[char] += 1
            else:
                chars_s1[char] = 1

        for char, amount in chars_s0.items():
            if char not in chars_s1 or chars_s1[char] != amount:
                return False
        return True

    if len(s0) != len(s1):
        return False

    s0_sorted = ''.join(sorted(list(s0)))
    s1_sorted = ''.join(sorted(list(s1)))
    return check_chars(s0_sorted, s1_sorted)

