def solve(N):
    """Returns the sum of digits in binary representation of the integer N."""
    binary_string = bin(N)[2:]
    return binary_string.zfill(len(binary_string) // 8)