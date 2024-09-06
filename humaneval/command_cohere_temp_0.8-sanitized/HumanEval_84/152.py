def solve(n):
    """
    :param n: Positive integer
    :return: Binary string representing the sum of digits in base 2
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if bin_sum.isdigit() else '0' + bin_sum
n = 1000