def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of digits of n
    """
    total_sum = 0
    num = str(n)
    while len(num) > 0:
        total_sum += int(num[0])
        num = num[1:]
        num = str(int(num) + num)
    return format(total_sum, 'b')