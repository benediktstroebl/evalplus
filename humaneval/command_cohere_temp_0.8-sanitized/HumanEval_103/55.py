def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0: 
        return -1 
    elif len(binary) & 1: 
        return int(binary, 2) 
    else: 
        return int(binary[0])