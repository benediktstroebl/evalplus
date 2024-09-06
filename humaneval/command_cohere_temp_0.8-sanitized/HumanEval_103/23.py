def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0 or diff % 2 == 0:
        return binary
    else:
        return -1