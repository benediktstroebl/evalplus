def solve(n):
    """
    :param n: Integer to be converted to binary
    :return: Binary string summing up to the total of digits in base 10
    """
    bin_str = bin(n)[2:]
    if not bin_str:
        return '0'
    else:
        return bin_str.count('1') % 2 == 0 and str(bin_str.count('1')) or '1'