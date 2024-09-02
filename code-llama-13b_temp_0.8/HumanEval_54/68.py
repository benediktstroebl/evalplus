

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

    def repl(match):
        nonlocal c
        c += 1
        return ''

    c = 0
    s1 = s1.replace(s0[0], '', len(s0) - 1)
    s1 = re.sub(s0[1:], repl, s1)

    return c == len(s0) - 1

