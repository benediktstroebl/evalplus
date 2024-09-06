def solve(N):
    """Returns the sum of digits in binary for the given integer N."""
    binary_string = bin(N)[2:]
    return binary_string.zfill(len(binary_string) + (len(binary_string) & 1))