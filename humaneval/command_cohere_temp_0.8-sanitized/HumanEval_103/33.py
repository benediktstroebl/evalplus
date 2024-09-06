def rounded_avg(n, m):
    bin_str = '-1' if n > m else bin(round((n + m) / 2))[2:]
    return bin_str if n <= m else -1