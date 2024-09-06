def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded_avg = round(avg)
    return bin(rounded_avg)[2:]