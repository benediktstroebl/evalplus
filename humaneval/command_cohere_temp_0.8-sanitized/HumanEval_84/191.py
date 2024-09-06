def solve(n):
    bin_str = "{0:b}".format(n)
    sum_bin = bin_str.count('1')
    return f"{sum_bin}"