def solve(n):
    """
    :param n: Integer to be transformed to binary string
    :return: Binary string of the sum of digits in base 2
    """
    # Your code here
    return '{:b}'.format(sum(int(d) for d in str(n)))