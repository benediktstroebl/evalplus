def solve(N):
    """Returns the sum of digits in binary representation of the given integer N."""
    bin_str = '{:b}'.format(N)
    sum_str = ''.join(bin_str.split('1'))
    return sum_str