def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer before returning it in binary form. 
    Returns -1 if n is greater than m.
    """ 
    # Calculate the average
    average = (n + m) // 2

    # Convert to binary and round
    binary_str = str(bin(round(average))[2:]).rjust(32, '0')
    
    # Return -1 if n is greater than m
    if n > m: return -1
    return binary_str