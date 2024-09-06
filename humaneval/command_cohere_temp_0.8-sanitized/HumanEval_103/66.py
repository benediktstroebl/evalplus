def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0: 
        return -1 
    if len(binary) & 1: 
        return int(binary, 2) 
    return int((binary[0] == '1') + int(binary[1:]), 2)