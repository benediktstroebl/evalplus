def solve(N):
    """
    :param N: integer
    :return: string of binary number
    """
    bin_str = bin(N)[2:]
    return bin_str.zfill(len(bin_str))