def solve(n):
    """
    :type n: int
    :param n: Should be a positive integer
    :return: A string of binary number
    """
    # Convert the decimal number to a binary string
    binary_representation = bin(n)[2:]
    # Convert each digit in the binary string to a decimal number
    decimal_digits = [int(digit) for digit in binary_representation]
    # Add up the decimal numbers to get the total sum
    total_sum = sum(decimal_digits)
    return bin(total_sum)[2:]