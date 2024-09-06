def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    # Convert the rounded average to binary
    binary_avg = bin(rounded_avg)[2:]  # Use the hexadecimal notation for binary conversion
    
    # Return the binary string or -1 if n is greater than m
    if n > m:
        return "-1"
    else:
        return binary_avg