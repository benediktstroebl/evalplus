def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string sum of digits of N
    """
    total_sum = 0
    tmp_n = str(n)
    while tmp_n:
        digit = tmp_n % 10
        total_sum += digit
        tmp_n = tmp_n // 10
    return format(total_sum, 'b')