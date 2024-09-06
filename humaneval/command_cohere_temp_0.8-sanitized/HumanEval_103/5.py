def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    if n > m:
        return -1
    while count <= m - n + 1:
        total += count
        count += 1
    rounded = round(total / (m - n + 1))
    if rounded == 0:
        return "0b0"
    binary = "{0:b}".format(rounded)
    return binary