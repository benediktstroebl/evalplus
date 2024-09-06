

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # the index of the first occurrence of the substring in the string
    first_occurrence = string.find(substring)
    # if the substring is not found, return 0
    if first_occurrence == -1:
        return 0
    # count the number of times the substring occurs in the string
    count = 1
    while first_occurrence != -1:
        # find the next occurrence of the substring in the string
        next_occurrence = string.find(substring, first_occurrence + 1)
        # increment the count
        count += 1
        # update the first_occurrence to the next occurrence of the substring
        first_occurrence = next_occurrence
    # return the count
    return count


