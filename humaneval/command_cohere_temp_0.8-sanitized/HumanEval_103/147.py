def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer, then convert it to binary.
    
    Args:
    - n (int): the starting integer.
    - m (int): the ending integer.
    
    Returns:
    - str: Binary string representation of the rounded average if n is not greater than m, 
          otherwise returns -1.
    """
    # Ensure n is not less than m to avoid errors
    if n > m:
        return -1
    
    total = 0
    num = n
    count = 1
    while num <= m:
        # Add num to the total when it's odd to achieve rounding
        if count % 2 == 1:
            total += num
        num += 1
        count += 1
    
    # Convert to binary, but ensure that the number of bits is limited to 32 for the exercise requirements.
    # Simply use the fist 32 bits of the decimal number
    # Convert to binary, and ensure result is positive
    return f"{total % (2**32)}b{bin(total % (2**32)[2:].zfill(32).count('1'))[2:]}"