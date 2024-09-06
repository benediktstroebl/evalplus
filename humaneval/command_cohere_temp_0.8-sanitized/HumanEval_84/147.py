def solve(N):
    """Returns the sum of digits in binary representation of the integer N."""
    bin_str = '{:b}'.format(N)
    return bin_str.count('1')