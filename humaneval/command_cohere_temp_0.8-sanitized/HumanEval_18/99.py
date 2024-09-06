def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    if not string or not substring:
        return 0
    
    count = 0
    tmp_str = string[:len(substring)]
    while tmp_str.startswith(substring):
        if tmp_str == substring:  # Avoid counting redundant cases
            count += 1
        tmp_str = tmp_str[1:]
    
    return count