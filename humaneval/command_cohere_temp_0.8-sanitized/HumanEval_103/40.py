def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    # Convert the rounded average to binary
    binary_avg = bin(rounded_avg)[2:]  # Remove '0b' prefix
    
    # Return -1 if n is greater than m
    return '-1' if n > m else binary_avg