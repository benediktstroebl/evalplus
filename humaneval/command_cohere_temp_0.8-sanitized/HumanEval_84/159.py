def solve(N):
    """Returns the sum of digits of N in binary."""
    binary_string = '0'
    while N:
        N, r = divmod(N, 2)
        binary_string += str(r)
    return binary_string