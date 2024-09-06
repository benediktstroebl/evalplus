def solve(N):
    """Returns the sum of digits in binary representation of the integer N."""
    bin_str = bin(N)[2:]
    return bin_str.zfill(len(bin_str))