def solve(n):
    bin_str = '{0:b}'.format(n)
    sum_list = [int(i) for i in bin_str]
    return '{0:b}'.format(sum(sum_list))