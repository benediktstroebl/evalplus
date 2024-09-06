def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string sum of digits of N
    """
    bin_sum = bin(n).count('1')
    return bin_sum
    
    # Test cases:
    # assert solve(1000) == "1"
    # assert solve(150) == "110"
    # assert solve(147) == "1100"