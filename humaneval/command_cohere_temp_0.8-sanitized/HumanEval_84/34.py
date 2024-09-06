def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string of the sum of digits in base 10
    :rtype: str
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if len(bin_sum) <= len(bin(n)[2:]) else bin_sum + '0' * (len(bin(n)[2:]) - len(bin_sum))