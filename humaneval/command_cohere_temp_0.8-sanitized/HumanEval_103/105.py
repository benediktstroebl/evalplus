def rounded_avg(n, m):
    bin_str = '{0:b}'.format(((n + m) // 2))
    return bin_str if n <= m else -1