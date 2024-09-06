def how_many_times(string, substring):
    if not string or not substring:
        return 0
    
    string = string.lower()
    substring = substring.lower()
    
    counter = 0
    n = len(substring)
    
    for i in range(len(string) - n + 1):
        if string[i:i+n] == substring:
            counter += 1
    
    return counter