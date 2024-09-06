def solve(n):
    """
    :type n: int
    :param n: Should be a positive integer
    :return: A string of binary number
    """
    # Convert integer to list of digits
    num_list = list(map(int, str(n)))
    # Convert list of digits to binary string
    bin_list = [bin(x)[2:][:1] for x in num_list]
    # Join binary strings together
    return ''.join(bin_list)