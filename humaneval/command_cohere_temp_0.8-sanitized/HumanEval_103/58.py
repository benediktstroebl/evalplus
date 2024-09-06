def rounded_avg(n, m):
    bin_str = "{0:b}".format(abs(n - m) // 2)
    if n > m:
        return -1
    return bin_str