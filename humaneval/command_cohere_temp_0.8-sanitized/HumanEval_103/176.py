def rounded_avg(n, m):
    if n > m:
        return -1
    total = (m + n) // 2
    count = m - n + 1
    avg = total // count
    return bin(round(avg))[2:]