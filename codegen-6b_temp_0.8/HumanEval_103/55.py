
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
    
    # make sure both n and m are of equal length
    n = (bin(n)[2:]).zfill(len(bin(m)))
    m = (bin(m)[2:]).zfill(len(bin(m)))
    
    # if n is greater than m, return -1
    if int(n, 2) > int(m, 2):
        return -1
    
    # if n < m, add zeros to n until it is the same length as m
    elif int(n, 2) < int(m, 2):
        n = n + ('0' * (len(m) - len(n)))
    
    # calculate the average
    average = sum([int(n[i]) * int(m[i]) for i in range(len(n))]) / (2 ** len(n))
    
    # convert the average to a binary number and return it
    return bin(average)[2:].zfill(len(bin(n)))