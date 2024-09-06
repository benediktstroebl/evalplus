def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0: 
        return -1 
    elif diff == 0: 
        return binary 
    else: 
        return '0b' + binary[1:]