def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of its digits.
    """
    total_sum = sum(map(int, str(n)))
    return format(total_sum, 'b')