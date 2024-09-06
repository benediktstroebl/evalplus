def solve(n):
    """
    :param n: Integer to be transformed to binary string
    :return: Binary string of the sum of digits in base 2
    """
    total_sum = 0
    num = str(n)
    for digit in num:
        total_sum += int(digit)
    
    binary_sum = bin(total_sum)[2:]
    return binary_sum