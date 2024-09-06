def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string sum of digits of N
    """
    bin_sum = bin(n).count('1')
    return bin_sum if bin_sum <= '1' else bin_sum[:-1]