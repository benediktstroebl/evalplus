def solve(n):
    """
    :param n: Integer to be converted to binary
    :return: Binary string summation of digits in n
    """
    bin_n = bin(n).replace("0b", "")
    sum_list = [int(digit) for digit in bin_n]
    sum_binary = bin(sum(sum_list))[2:]
    return sum_binary