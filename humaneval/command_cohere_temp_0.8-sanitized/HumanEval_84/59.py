def solve(n):
    """Returns the sum of digits in binary representation of the given integer n."""
    bin_str = bin(n)[2:]
    return bin_str.count('1')