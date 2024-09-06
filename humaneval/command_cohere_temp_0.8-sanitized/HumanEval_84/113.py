def solve(N):
    bin_str = bin(N)[2:]
    sum_list = list(map(int, bin_str))
    return ''.join(map(str, sum_list))