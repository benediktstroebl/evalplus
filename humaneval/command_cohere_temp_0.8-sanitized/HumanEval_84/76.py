def solve(n):
    """
    :param n: Positive integer
    :return: Binary string summing up to the total sum of digits of n
    """
    bin_str = bin(n)[2:]
    if not bin_str:
        return '0'
    total_sum = sum([int(x) for x in bin_str])
    return format(total_sum, 'b')