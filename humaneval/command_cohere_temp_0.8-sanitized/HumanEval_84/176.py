def solve(n):
    bin_str = '{:b}'.format(n)
    sum_in_bin = bin_str.count('1')
    return f'{sum_in_bin}'