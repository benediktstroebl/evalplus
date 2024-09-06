def solve(n):
    """
    :param n: Integer to be transformed to binary string
    :return: Binary string of the integer
    """
    bin_n = bin(n)
    return bin_n[2:][:len(bin(n))]