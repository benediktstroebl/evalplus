def solve(n):
    bin_str = bin(n)[2:]
    sum_list = [int(x) for x in bin_str if x != '0']
    return '{0:b}'.format(sum(sum_list))