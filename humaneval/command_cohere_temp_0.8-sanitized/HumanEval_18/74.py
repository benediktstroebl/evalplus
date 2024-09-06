def how_many_times(string, substring):
    if not string or not substring:
        return 0
    
    n, m = len(string), len(substring)
    
    count = 0
    n_sub = 0
    
    for i in range(m):
        n_sub = n - m + 1
        sub = substring[:i] + substring[i+1:]
        
        count += n_sub - (string.count(sub) if sub in string else 0)
        if count < 0:
            count = 0
    
    return count