

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    current_index = 0
    overlaps = 0
    while current_index < len(string):
        current_index = string.find(substring, current_index)
        if current_index == -1:
            return overlaps
        overlaps += 1
        current_index += 1

