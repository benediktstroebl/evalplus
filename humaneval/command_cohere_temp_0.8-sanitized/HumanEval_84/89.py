def solve(N):
    """Return the sum of digits in binary representation."""
    bin_str = '{:b}'.format(N)
    sum_str = ''.join(bin_str.split('1'))
    return sum_str