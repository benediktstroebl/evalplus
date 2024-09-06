def solve(n):
    bin_str = "{0:b}".format(n)
    sum_list = [int(i) for i in bin_str]
    sum_str = ''.join(map(str, sum_list))
    return sum_str