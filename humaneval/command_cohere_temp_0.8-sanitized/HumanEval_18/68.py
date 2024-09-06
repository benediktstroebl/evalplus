def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == substring:
                count += 1
    return count