def solve(N):
    """Return the sum of digits in binary representation."""
    bin_str = '{:b}'.format(N)
    return bin_str.count('1')