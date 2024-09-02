

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string:
        return 0
    occurences = []
    for letter in substring:
        if letter in string:
            pos = string.find(letter)
            occurences.append(pos)
    return len(occurences)
