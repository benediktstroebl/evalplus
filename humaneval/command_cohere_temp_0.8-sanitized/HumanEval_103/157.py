def rounded_avg(n, m):
    """
    Compute the average of integers from n to m (inclusive), round to the nearest integer, 
    and convert to binary. Returns -1 if n > m.
    """
    if n > m:
        return -1
    total = (n + m) // 2  # Average is the midpoint between n and m
    return format(round(total), 'b')