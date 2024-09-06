

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(string) == 0 or len(substring) == 0:
        return 0
    # if substring is longer than string, return 0
    if len(substring) > len(string):
        return 0

    # set the count to zero
    count = 0
    # index of substring in string
    index = 0
    # while loop that will iterate through the string
    while index < len(string) - len(substring) + 1:
        # loop through each character of the substring
        for i in range(0, len(substring)):
            # if string's char at current index is equal to substring char at current index
            if string[index + i] != substring[i]:
                break
            # if substring is found, add 1 to count and skip to next instance of substring in string
            if i == len(substring) - 1:
                count += 1
                index += len(substring)
        index += 1
    return count

