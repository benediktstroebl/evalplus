def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    tmp_string = string.lower()
    tmp_substring = substring.lower()
    while tmp_string:
        if tmp_string.startswith(tmp_substring):
            count += 1
            tmp_string = tmp_string[len(tmp_substring):]
        else:
            tmp_string = tmp_string[1:]
    return count