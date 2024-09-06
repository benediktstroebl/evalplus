def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    # Convert the result to binary
    binary_representation = bin(rounded_avg)[2:]
    
    # Return -1 if n is greater than m
    if n > m:
        return -1
    
    return binary_representation