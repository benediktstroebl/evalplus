def rounded_avg(n, m):
    bin_str = '-1' if n > m else '{:.0b}'.format(int((n + m) / 2))
    return bin_str