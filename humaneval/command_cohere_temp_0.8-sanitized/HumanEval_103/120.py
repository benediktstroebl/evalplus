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
    
    total = (n + m) // 2
    count = m - n + 1
    average = total // count
    return bin(round(average))[2:]