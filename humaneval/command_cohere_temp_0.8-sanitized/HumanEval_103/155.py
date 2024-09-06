def rounded_avg(n, m):
    if n > m:
        return -1
    sum_ = 0
    for i in range(n, m + 1):
        sum_ += i
    avg = int(round(sum_ / (m - n + 1)))
    return f"0b{bin(avg)[2:]}"