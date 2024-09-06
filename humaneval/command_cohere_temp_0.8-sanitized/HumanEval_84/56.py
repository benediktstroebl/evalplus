def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string sum of decimal representation of n
    """
    return str(bin(sum([int(d) for d in str(n)]))[2:])
n = 1000