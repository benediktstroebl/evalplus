def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :type n: int
    :return: Binary string sum of digits of N
    :rtype: str
    """
    bin_sum = bin(n)[2:]    
    return bin_sum