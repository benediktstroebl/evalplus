def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string sum of digits of N
    """
    total_sum = 0
    tmp_n = n
    while tmp_n > 0:
        digit = tmp_n % 2
        total_sum += digit
        tmp_n //= 2
    # Convert to string and append leading zero if necessary
    return str(total_sum) + '0' * (len(str(n)) - len(str(total_sum)))