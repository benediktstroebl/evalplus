def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string sum of digits of N
    :rtype: str
    """
    # Your code here!
    bin_n = bin(n).replace("0b", "")
    return bin_n if len(bin_n) == 1 else bin_n[:1]