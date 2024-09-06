def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of digits of n
    """
    total_sum = 0
    num = str(n)
    for digit in num:
        total_sum += int(digit)
    return format(total_sum, 'b')