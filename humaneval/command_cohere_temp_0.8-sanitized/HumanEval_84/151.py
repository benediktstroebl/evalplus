def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string sum of digits of N
    :rtype: str
    """
    # Your code here!
    return bin(sum([int(d) for d in str(n)]))[2:]