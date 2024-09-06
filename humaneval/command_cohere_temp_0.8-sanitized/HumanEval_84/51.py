def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string sum of digits of N
    """
    bin_sum = 0
    ret = ""
    
    for digit in str(n):
        bin_sum += int(digit)
        
        ret = ret + str(bin_sum)
        
    return ret