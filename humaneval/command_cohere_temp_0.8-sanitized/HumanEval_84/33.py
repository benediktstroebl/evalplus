def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string of the sum of digits in base 10
    :rtype: str
    """
    # Convert the integer to a string to remove trailing zeros
    bin_str = str(n).bex()
    # Convert the string to an integer to remove leading zeros
    bin_str = int(bin_str)
    
    return bin(bin_str).replace('0b', '')