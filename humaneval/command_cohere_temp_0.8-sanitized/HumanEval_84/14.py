def solve(N):
    bin_str = '{:b}'.format(N)
    sum_str = ''.join(bin_str.split('1'))
    return sum_str if sum_str.isdigit() else '0'