def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    if not string or not substring:
        return 0
    count = 0
    tmp_string = string[:]
    while tmp_string:
        if tmp_string.startswith(substring):
            count += 1
            tmp_string = tmp_string[len(substring):]
        else:
            break
    return count