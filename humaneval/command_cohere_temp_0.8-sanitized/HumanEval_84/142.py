def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string of the sum of digits in base 10
    :rtype: str
    """
    # Convert the number to a string
    num_str = str(n)
    # Initialize variables to store the sum of digits in binary and decimal respectively
    bin_sum = '0'
    dec_sum = 0
    # Loop through each digit in the number and add it to the decimal sum
    for digit in num_str:
        dec_sum += int(digit)
        # Convert the decimal sum to a binary string and concatenate it to the bin_sum variable
        bin_sum = bin(dec_sum)[2:].zfill(len(bin_sum))
    return bin_sum