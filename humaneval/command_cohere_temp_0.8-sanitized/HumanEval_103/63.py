def rounded_avg(n, m):
    binary_str = '-1'
    avg = (n + m) // 2

    if n <= m:
        avg = round(avg)
        binary_str = bin(avg)[2:]
        return binary_str
    else:
        return binary_str