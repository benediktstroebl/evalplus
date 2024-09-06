def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    else:
        return bin(round(avg))[2:]