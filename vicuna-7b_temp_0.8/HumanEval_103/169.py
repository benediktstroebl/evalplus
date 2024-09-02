
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
    # handle the special case when m is 0
    if m == 0:
        return 0
    
    # handle the special case when n is greater than m
    if n > m:
        return -1
    
    # use binary numbers to represent n and m
    binary_n = str(n)[2:]
    binary_m = str(m)[2:]
    
    # use the while loop to iterate through n and m
    result = 0
    while binary_n > binary_m:
        # extract the leftmost digit of binary_n and binary_m
        digit1 = binary_n[-1]
        digit2 = binary_m[-1]
        
        # check if the two digits are different
        if digit1 == digit2:
            # return 0
            return 0
        elif digit1 > digit2:
            # return 1
            return 1
        else:
            # add 1 to the leftmost digit of binary_n and binary_m
            binary_n = binary_n[:-1]
            binary_m = binary_m[:-1]
            
            # move to the next iteration
            continue
            
    # return the binary representation of the average of n and m
    return "0b" + binary_n + binary_m[1:]
