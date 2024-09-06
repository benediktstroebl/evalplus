def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded_avg = bin(round(avg))[2:]
    return rounded_avg