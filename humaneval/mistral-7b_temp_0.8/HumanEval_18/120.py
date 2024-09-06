

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if string == '' or substring == '':
        return 0
    # number of times the substring is present
    count = 0
    # index for searching
    start_index = 0
    while True:
        # search for next occurrence of the substring
        index = string.find(substring, start_index)
        # if substring not found at all
        if index == -1:
            break
        # update start index for next search
        start_index = index + 1
        # increment count
        count += 1
    return count

