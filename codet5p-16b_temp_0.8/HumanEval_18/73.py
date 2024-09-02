

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    assert string, 'String cannot be empty'
    assert substring, 'Substring cannot be empty'
    assert len(substring) <= len(string)

    count = 0
    start_index = 0
    while start_index < len(string):
        end_index = string.find(substring, start_index)
        if end_index == -1:
            return count
        count += 1
        start_index = end_index + 1

