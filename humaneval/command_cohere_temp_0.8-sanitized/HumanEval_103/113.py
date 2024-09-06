def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = ((n + m) // 2) if n != m else n if n > m else m
    rounded_avg = round(avg)
    
    # Convert the integer to binary
    binary = bin(rounded_avg)[2:]
    
    # Return -1 if n is greater than m
    return "-1" if n > m else binary