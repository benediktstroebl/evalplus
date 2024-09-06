def solve(N):
    """
    :type N: int
    :param N: integer
    :rtype: str
    """
    bin_str = bin(N)[2:]
    sum_list = []
    for digit in bin_str:
        sum_list.append(int(digit))
    total_sum = sum(sum_list)
    return format(total_sum, 'b')