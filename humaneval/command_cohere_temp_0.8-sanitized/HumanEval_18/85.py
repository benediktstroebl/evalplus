def how_many_times(string, substring):
    if not string or not substring:
        return 0
    
    if len(string) < len(substring):
        return 0
    
    count = 0
    start = 0
    step = 1
    while start < len(string) - len(substring) + 1:
        try:
            if string[start:start + len(substring)] == substring:
                count += 1
        except UnicodeDecodeError:  # Handle bytes when trying to compare with a string in ASCII
            if str(string[start:start + len(substring)]) == str(substring):
                count += 1
        start += step
        step = -1 if (start + step) >= len(string) else 1
    return count