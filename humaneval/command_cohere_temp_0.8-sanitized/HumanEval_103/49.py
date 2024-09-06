def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer. Convert that integer to binary and 
    return as a string. If n is greater than m, return -1 as a string.
    """
    if n > m:
        return "-1"
    total = (n + m) // 2  # Average the sum of integers from n through m
    rounded = round(total)
    binary = bin(rounded)[2:]  # Convert to binary and remove '0b'
    return binary