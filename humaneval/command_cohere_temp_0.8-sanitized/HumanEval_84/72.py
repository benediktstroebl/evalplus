def solve(N):
    """
    Get the sum of digits in binary representation of the given integer N.
    """
    bin_str = bin(N)[2:]
    sum_digits = bin_str.count('1')
    return str(sum_digits)