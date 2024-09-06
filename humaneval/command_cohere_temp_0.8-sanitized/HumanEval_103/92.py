def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    binary_str = bin(round(avg))[2:]
    return binary_str if binary_str[0] != '0' else binary_str[1:]