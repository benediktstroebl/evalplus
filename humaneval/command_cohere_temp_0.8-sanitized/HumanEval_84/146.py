def solve(n):
    """
    :param n: Integer to be transformed to binary string
    :return: Binary string of the sum of digits in base 10
    """
    bin_str = '{:b}'.format(n)
    sum_list = [int(i) for i in bin_str]
    sum_bin = bin(sum(sum_list))[2:][:len(bin_str)]
    return sum_bin