def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded_avg = bin(round(avg)).replace('0b', '')
    return rounded_avg