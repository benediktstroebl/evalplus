def solve(n):
    bin_str = "{0:b}".format(n)
    sum_str = "".join(bin_str.split('1'))
    return sum_str