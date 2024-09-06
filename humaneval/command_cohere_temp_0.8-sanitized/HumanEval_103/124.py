def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer before returning it in binary.
    
    Args:
    - n (int): the starting integer.
    - m (int): the ending integer.
    
    Returns:
    - str: Binary string representation of the rounded average. Returns -1 if n > m.
    """
    if n > m:
        return -1
    
    total = (n + m) // 2  # Average is the middle point between n and m.
    return format(round(total), 'b').rjust(64, '0')