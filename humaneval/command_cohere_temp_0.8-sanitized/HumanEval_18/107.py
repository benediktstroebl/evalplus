def how_many_times(string, substring):
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    if not string or not substring:
        return 0
    
    counter = 0
    length = len(substring)
    
    for i in range(len(string) - length + 1):
        if string[i:i+length] == substring:
            counter += 1
    
    return counter