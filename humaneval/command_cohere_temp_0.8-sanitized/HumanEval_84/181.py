def solve(n):
    """
    :param n: Integer to be transformed to binary sum of digits
    :return: String binary representation of sum of digits of n
    """
    total_sum = 0
    for digit in str(n):
        total_sum += int(digit)
    return format(total_sum, 'b')