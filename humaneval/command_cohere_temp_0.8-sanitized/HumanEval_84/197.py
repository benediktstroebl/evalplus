def solve(N):
    """Returns the sum of digits in binary for the given integer N."""
    digs = bin(N).count('1')
    return digs