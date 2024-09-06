def solve(N):
    """
    :param N: integer
    :return: string
    """
    bin_str = bin(N)[2:]
    sum_str = ''.join(str(int(bit) for bit in bin_str if int(bit)))
    return sum_str