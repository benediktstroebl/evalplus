def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = ((n + m) // 2)
    avg_rounded = round(avg)
    
    # Convert the rounded average to binary
    binary_avg = bin(avg_rounded)[2:]  # Remove the '0b' prefix
    
    # Return -1 if n is greater than m
    return binary_avg if n <= m else -1