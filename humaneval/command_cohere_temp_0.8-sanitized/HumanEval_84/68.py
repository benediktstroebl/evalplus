def solve(n):
    """
    :param n: Integer to be transformed to binary and sum its digits
    :return: String of binary number of the sum of digits of n
    """
    total_sum = 0
    n = str(n)
    for digit in n:
        total_sum += int(digit)
    return bin(total_sum).replace('0b', '')