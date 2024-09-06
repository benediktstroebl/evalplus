def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String - Binary string of the sum of the digits of n
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if len(bin_sum) <= len(str(n)) else bin_sum[:len(str(n))]