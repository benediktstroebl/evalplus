def solve(n):
    """Returns the sum of digits in binary representation of the given integer n."""
    binary_string = '0' * (len(bin(n)) - 2)
    result = 0
    while n:
        n, r = divmod(n, 2)
        result += r
        binary_string = str(r) + binary_string
    return binary_string + str(result)