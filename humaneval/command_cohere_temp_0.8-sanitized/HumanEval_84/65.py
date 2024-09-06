def solve(N):
    """
    :type N: int
    :param N: integer
    :rtype: str
    """
    binary_str = bin(N)[2:]
    return binary_str.zfill(len(binary_str) // 2)