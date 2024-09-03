def rounded_avg(n, m):
    """
    Compute the average of integers from n through m (including n and m), round the answer to the nearest integer, 
    and convert it to binary.
    Args: 
        n, m: two positive integers
    Returns: 
        str: binary representation of the rounded average of the integers from n through m
    """
    if n > m:
        return '1'
    else:
        return '0b' + str(round(n + m, 1))[2:]