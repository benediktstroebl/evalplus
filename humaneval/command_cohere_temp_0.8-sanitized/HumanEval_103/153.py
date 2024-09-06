def rounded_avg(n, m):
    bin_str = '-1' if n > m else '{0:b}'.format(((n + m) // 2))
    return bin_str if n <= m else -1