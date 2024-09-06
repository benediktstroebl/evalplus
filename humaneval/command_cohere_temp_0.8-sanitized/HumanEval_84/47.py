def solve(N):
    """Return the sum of digits in binary for a given positive integer N."""
    bin_str = bin(N)[2:]
    return bin_str.zfill(len(bin_str))