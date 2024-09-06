def solve(n):
    """
    :param n: Positive Integer N
    :return: Binary string of the sum of digits of N
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if len(bin_sum) <= len(str(n)) else bin_sum[len(str(n))::]