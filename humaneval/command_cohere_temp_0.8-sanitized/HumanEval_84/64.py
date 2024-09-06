def solve(n):
    """
    :type n: int
    :param n: Integer to be converted to binary string
    :return: Binary string sum of digits of n
    """
    return ''.join(format(n, 'b'))