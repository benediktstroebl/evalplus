def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    tmp_str = string.lower()
    tmp_sub = substring.lower()
    while tmp_str:
        if tmp_str.startswith(tmp_sub):
            count += 1
            tmp_str = tmp_str[len(tmp_sub):]
        else:
            break
    return count