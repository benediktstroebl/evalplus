def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    binary_string = bin(round(avg))[2:]
    return binary_string if binary_string.isalpha() else '0b' + binary_string