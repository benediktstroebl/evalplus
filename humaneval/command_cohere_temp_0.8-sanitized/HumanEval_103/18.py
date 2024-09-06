def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    # Convert the result to binary and return
    if rounded_avg == -1:
        return "-1"
    else:
        return f"0b{bin(rounded_avg)[2:]}"