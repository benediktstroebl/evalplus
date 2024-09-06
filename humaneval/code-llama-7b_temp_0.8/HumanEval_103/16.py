
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
    # check if n is greater than m
    if n > m:
        return -1
    # calculate avg
    avg = (n+m)/2
    # convert to binary
    bin_n = bin(int(avg))
    # check if avg is even or odd
    if avg%2==0:
        # round to nearest even
        if int(bin_n[2]) >=5:
            bin_n = str(int(bin_n[2])+1)
        else:
            bin_n = str(int(bin_n[2]))
    else:
        # round to nearest even
        if int(bin_n[2]) >=5:
            bin_n = str(int(bin_n[2])+2)
        else:
            bin_n = str(int(bin_n[2])+1)
    
    return bin_n
