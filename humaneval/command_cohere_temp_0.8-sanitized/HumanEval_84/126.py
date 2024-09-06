def solve(n):
    """
    :param n: Integer to be transformed to binary string
    :return: Binary string of the sum of digits in base 2
    """
    total_sum = 0
    for digit in str(n):
        total_sum += int(digit)
    binary_string = bin(total_sum)[2:]
    return binary_string