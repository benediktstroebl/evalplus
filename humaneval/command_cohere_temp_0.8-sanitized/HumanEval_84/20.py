def solve(n):
    """
    :param n: Integer to be transformed to binary sum of digits
    :return: String binary representation of sum of digits of n
    """
    return '{:b}'.format(sum(map(int, str(n))))