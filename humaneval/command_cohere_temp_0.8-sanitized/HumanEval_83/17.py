def starts_one_ends(n):
    # Create a list to store the counts of starting or ending with 1
    counts = [0] * (n + 1)
    
    # Count numbers that start with 1
    for i in range(1, n + 1):
        if i == 1:
            counts[i] = 1
        else:
            counts[i] = counts[i - 2] + counts[i - 1]
    
    # Count numbers that end with 1
    tot = 1
    for i in range(n, 0, -1):
        if i == n:
            counts[i] = 1
        else:
            counts[i] += counts[i + 2] + tot
        tot += 1
    
    return counts[n]