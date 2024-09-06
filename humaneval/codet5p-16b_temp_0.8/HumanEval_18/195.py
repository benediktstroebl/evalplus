

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    counter: int = 0
    i: int = 0
    while i < len(string):
        j: int = 0
        while j < len(substring) and i+j < len(string):
            if string[i+j]!= substring[j]:
                break
            j += 1
        if j == len(substring):
            counter += 1
            i += len(substring)
        else:
            i += 1
    return counter
