def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    if n > m:
        return -1
    while count <= m - n + 1:
        total += count
        count *= 2
    return format(round(total / (m - n + 1)), 'b')