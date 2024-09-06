def how_many_times(string, substring):
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    n = len(string)
    m = len(substring)
    count = 0
    idx = 0
    while idx < n - m + 1:
        if string[idx:idx+m] == substring:
            count += 1
            idx += 1
        else:
            idx += 1
        # To handle overlapping cases, we don't increment idx here, and continue searching in the remainder of the loop.
    return count