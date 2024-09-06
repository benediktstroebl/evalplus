def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    if not string or not substring:
        return 0
    
    count = 0
    i = 0
    j = 0
    
    while i < len(string) and j < len(substring):
        if string[i] == substring[j]:
            count += 1
            i += 1
            j += 1
        elif string[i] < substring[j]:
            i += 1
        else:
            j += 1
    
    return count