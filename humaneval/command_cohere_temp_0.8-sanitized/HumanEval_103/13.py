def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer, then convert it to binary.
    
    Args:
    - n (int): the starting integer.
    - m (int): the ending integer.
    
    Returns:
    - str: Binary string representation of the rounded average if n is not greater 
          than m, otherwise returns -1.
    """
    # Ensure n is not less than m to avoid errors
    if n > m:
        return -1
    
    total = 0
    count = 0
    for i in range(n, m + 1):
        total += i
        count += 1
    # Round down to nearest integer
    rounded_avg = total // count
    # Convert to binary
    return f"0b{bin(rounded_avg)[2:]}"