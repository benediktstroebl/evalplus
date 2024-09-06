def solve(N):
    """
    :param N: integer
    :return: string
    """
    bin_sum = bin(N).count('1')
    return f'{bin_sum:b}'