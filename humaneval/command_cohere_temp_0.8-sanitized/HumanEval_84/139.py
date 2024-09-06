def solve(n):
    """
    :param n: Integer to be transformed to binary sum of digits
    :return: Binary string of the sum of the digits in decimal
    """
    total_sum = 0
    num = str(n)
    for digit in num:
        total_sum += int(digit)
    
    return format(total_sum, 'b')