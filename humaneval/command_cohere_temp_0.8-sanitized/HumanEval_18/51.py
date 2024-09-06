def how_many_times(string, substring):
    if not string or not substring:
        return 0
    
    string = string.lower()
    substring = substring.lower()
    
    count = string.count(substring)
    
    return count