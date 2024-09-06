def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    idx = 0
    while idx < len(string) - len(substring) + 1:
        found = True
        for i in range(len(substring)):
            if string[idx + i] != substring[i]:
                found = False
                break
        if found:
            count += 1
        idx += 1
    return count