

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
    length = len(string)
    ss_length = len(substring)
    for i in range(length):
        if i + ss_length <= length:
            if string[i] == substring[0]:
                if string[i:i + ss_length] == substring:
                    count += 1
    return count

