def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    idx = 0
    while idx < len(string):
        idx2 = string.find(substring, idx)
        if idx2 == -1:
            break
        count += 1
        idx = idx2 + 1
    return count