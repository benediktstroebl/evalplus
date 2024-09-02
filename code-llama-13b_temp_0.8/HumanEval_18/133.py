

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # length of substring to check
    n = len(substring)
    # count
    count = 0
    # if string is empty return 0
    if string == '':
        return 0
    # set start and end to zero
    start = 0
    end = 0
    # loop over the string
    while end < len(string):
        # if the substring is equal to our desired substring then count it
        if string[start:end + n] == substring:
            count += 1
        # set the end to next position
        end += 1
        # if the end position is bigger than the length of the string
        if end >= len(string):
            # reset the start position and end to the beginning
            start = end
            end = start + 1
    # return count
    return count

