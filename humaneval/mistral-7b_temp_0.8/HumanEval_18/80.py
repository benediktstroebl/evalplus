

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if len(substring) > len(string):
        return 0
    count = 0
    left = 0
    for right in range(len(string)):
        if string[right] == substring[0]:
            count += 1
            for i in range(len(substring)):
                if string[left + i] != substring[i]:
                    break
                if i == len(substring) - 1:
                    count += 1
                    left += 1
                    break
        else:
            left += 1
    return count

