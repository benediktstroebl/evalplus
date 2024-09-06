def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    # Convert the result to binary and return
    binary_representation = bin(rounded_avg)[2:]
    if binary_representation.count('1') > 1:
        return "-1"
    else:
        return binary_representation