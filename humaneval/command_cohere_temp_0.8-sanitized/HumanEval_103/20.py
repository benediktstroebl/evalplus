def rounded_avg(n, m):
    if n > m:
        return -1
    sum_ = 0
    count = 0
    for i in range(n, m + 1):
        sum_ += i
        count += 1
    avg = round(sum_ / count)
    return f"0b{bin(avg)[2:]}"