def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer before returning it in binary format. 
    Returns -1 if n is greater than m.
    """ 
    if n > m:
        return -1
    total = (n + m) // 2  # Average is the midpoint between n and m
    return formatted_integer(total)
def formatted_integer(num):
    return '0b' + bin(round(num))[2:].zfill(32)