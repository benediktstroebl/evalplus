def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string of the sum of the digits of n
    """
    # Convert integer to binary
    bin_n = bin(n)[2:]
    # Remove leading zeros
    bin_n = bin_n.lstrip('0')
    return bin_n