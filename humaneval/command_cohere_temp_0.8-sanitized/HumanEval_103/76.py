def rounded_avg(n, m):
    if n > m:
        return -1
    sum_ = sum(range(n, m + 1))
    avg = round(sum_ / (m - n + 1))
    return bin(avg)[2:]