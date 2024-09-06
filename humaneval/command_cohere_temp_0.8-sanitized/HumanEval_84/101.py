def solve(N):
    """Returns the sum of digits in binary form for a given positive integer N."""
    binary_string = '1'
    while N > 0:
        N, r = divmod(N, 2)
        binary_string += str(r)
    return binary_string