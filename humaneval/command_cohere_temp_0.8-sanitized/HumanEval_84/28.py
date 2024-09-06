def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string of the sum of the digits of n
    """
    total_sum = 0
    num = str(n)
    for digit in num:
        total_sum += int(digit)
    
    bin_total = bin(total_sum)[2:]
    return bin_total