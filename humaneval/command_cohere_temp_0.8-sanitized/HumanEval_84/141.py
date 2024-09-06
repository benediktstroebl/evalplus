def solve(N):
    """Returns the sum of digits in binary form for a given positive integer N."""
    binary_sum = bin(N).count('1')
    return binary_sum if binary_sum < 10 else '1' + bin(binary_sum - 1)[2:]