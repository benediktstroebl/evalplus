def rounded_avg(n, m):
    binary_str = '-1' if n > m else bin(round((n + m) / 2)).replace('0b', '')
    return binary_str if n != m else binary_str + '1' if n % 2 == 1 else binary_str + '0'