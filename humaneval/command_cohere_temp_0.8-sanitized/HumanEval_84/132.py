def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String - Binary representation of the sum of digits of n
    """
    total_sum = sum(map(int, str(n)))
    return bin(total_sum)[2:]