def solve(n):
    """
    :type n: int
    :param n: integer
    :rtype: str
    """
    binary_str = ''
    total_sum = 0
    while n > 0:
        digit = n % 2
        total_sum += digit
        binary_str = str(digit) + binary_str
        n //= 2
    return format(total_sum, 'b') + binary_str