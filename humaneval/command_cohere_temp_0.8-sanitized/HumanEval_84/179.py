def solve(n):
    """
    :type n: int
    :param n: Should be a positive integer
    :return: A string of binary number
    """
    # Your code here
    bin_str = bin(n)[2:]
    return bin_str.replace('0', '').replace('1', '01')