def solve(N):
    """
    :param N: integer
    :return: string
    """
    bin_str = bin(N)[2:]
    return bin_str.replace('0', '').strip('1')