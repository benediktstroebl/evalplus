def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String - Binary string of the sum of digits
    """
    total_sum = 0
    # Convert integer to binary string
    bin_str = bin(n)[2:]
    while bin_str:
        digit = int(bin_str[0])
        total_sum += digit
        bin_str = bin_str[1:]
    # Convert total sum to binary string
    sum_in_binary = bin(total_sum)[2:]
    return sum_in_binary