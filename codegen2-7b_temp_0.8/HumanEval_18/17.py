

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    for i, _ in enumerate(string):
        for j, _ in enumerate(string[i:]):
            if substring == string[i+j:i+j+len(substring)]:
                count += 1
                break
    return count

