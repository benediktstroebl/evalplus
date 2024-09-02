
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    bin_str = "{:064b}".format(n)
    while bin_str[-1] == '0':
        bin_str = bin_str[:-1]
    bin_str = bin_str + "{:064b}".format(m)
    num = 0
    for i in range(len(bin_str)):
        num = num * 2 + int(bin_str[i])
    return "{:064b}".format(num / (len(bin_str) + 1
