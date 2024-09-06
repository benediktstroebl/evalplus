def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of digits of n
    """
    total_sum = 0
    temp_n = str(n)
    while temp_n:
        digit = temp_n[-1]
        total_sum += int(digit)
        temp_n = temp_n[:-1]
    return format(total_sum, 'b')