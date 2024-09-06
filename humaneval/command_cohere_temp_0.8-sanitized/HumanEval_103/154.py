def rounded_avg(n, m):
    binary_str = '-1' if n > m else bin(round((n + m) / 2)).split('b')[1]
    return binary_str if n != m else binary_str[0]