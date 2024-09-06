def solve(n):
    """
    :param n: Integer to be transformed to binary and have its digits summed
    :return: Binary string summation of integer
    """
    bin_n = bin(n).replace("0b", "")
    return bin_n if len(bin_n) <= 8 else bin_n[0:8]