def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer before converting it to binary. 
    Returns -1 if n is greater than m.
    """
    if n > m:
        return -1
    total = (n + m) // 2  # Average is the middle number
    return binary(total)
def binary(n):
    """Convert a number to binary string format."""
    return f"0b{bin(n)[2:]}"