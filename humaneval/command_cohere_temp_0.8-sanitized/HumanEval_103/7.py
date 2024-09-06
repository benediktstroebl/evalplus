def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer before returning it in binary format. 
    Returns -1 if n is greater than m.
    """ 
    # Ensure n is not larger than m
    if n > m:
        return -1
    
    total = 0
    num = n
    count = 1
    while num <= m: 
        total += num
        num += 1
        count += 1
    
    # Calculate the average and round it to the nearest integer
    avg = total // count
    rounded_avg = bin(round(avg))[2:]
    return rounded_avg