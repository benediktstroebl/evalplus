def solve(n):
    """
    :param n: Integer to be converted to binary
    :return: Binary string sum of digits of n
    """
    bin_str = bin(n)[2:]
    return bin_str.replace('0b', '').replace('0', '').strip()