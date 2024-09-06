def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string of the sum of its digits.
    """
    total_sum = 0
    num = str(n)
    for digit in num:
        total_sum += int(digit)
    
    # Convert total sum to binary string
    binary_str = bin(total_sum)[2:]
    return binary_str