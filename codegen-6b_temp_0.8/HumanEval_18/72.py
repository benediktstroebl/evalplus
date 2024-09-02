

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
    prev = -1
    while True:
        next = string.find(substring, prev + 1)
        if next == -1:
            break
        if next != -1:
            count += 1
        prev = next
    return count

