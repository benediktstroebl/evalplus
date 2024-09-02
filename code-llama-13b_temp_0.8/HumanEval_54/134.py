

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
    # Hint: Use the Counter data structure.
    # In this case it is better to use the built-in Counter than create a custom one.
    # It will do all the work for you.
    # http://docs.python.org/3/library/collections.html#collections.Counter
    from collections import Counter
    # Note: Counter() converts a string to a list automatically.
    return Counter(s0) == Counter(s1)

