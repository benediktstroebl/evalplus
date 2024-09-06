def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :type n: int
    :return: Binary string of the sum of digits of n
    :rtype: str
    """
    # Your code here
    return bin(sum([int(d) for d in str(n)]))[2:]