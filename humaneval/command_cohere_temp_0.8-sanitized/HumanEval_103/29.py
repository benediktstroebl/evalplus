def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer, then convert it to binary.
    """
    # Ensure n is the larger number
    if n < m:
        temp = n
        n = m
        m = temp

    total = n + (m-n) // 2
    rounded = round(total / (m-n))

    if n == m:
        return "0b0"
    elif rounded == int(rounded):
        return f"0b{bin(rounded)[2:]}"
    else:
        return -1