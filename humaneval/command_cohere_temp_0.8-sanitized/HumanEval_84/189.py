def solve(n):
    """Returns the sum of digits in binary representation of the integer n."""
    return ''.join(bin(d).count('1') for d in map(int, str(n)))