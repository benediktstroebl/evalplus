def how_many_times(string, substring):
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            count += 1
    return count