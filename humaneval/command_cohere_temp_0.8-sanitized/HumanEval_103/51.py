def rounded_avg(n, m):
    binary_str = '-1'
    avg = (n + m) // 2

    if n <= m:
        avg = round(avg)
        binary_str = bin(avg)[2:]

        if len(binary_str) < 2:
            binary_str = '0' + binary_str
    return binary_str