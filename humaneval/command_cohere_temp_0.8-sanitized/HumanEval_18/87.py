def how_many_times(main_string, substring):
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    if not main_string or not substring:
        return 0
    
    count = 0
    pos = 0
    
    while pos < len(main_string):
        temp_pos = main_string.find(substring, pos)
        if temp_pos == -1:
            break
        count += 1
        pos = temp_pos + 1
    
    return count