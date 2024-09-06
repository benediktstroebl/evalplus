def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes the starting digits,
    # so the largest possible n-digit number that fits in a list of length n is
    # 9999...999 (n digits) or 10^n - 1.
    counts = [0] * (10 ** n - 1)
    
    # Count the numbers that start with 1
    half_n = n // 2
    for i in range(1, half_n + 1):
        counts[10 ** (i - 1) - 1] = counts[10 ** (i - 1) - 1] + 1
    
    # Count the numbers that end with 1
    for i in range(half_n - 1, 0, -1):
        counts[10 ** i - 1] = counts[10 ** i - 1] + 1
    
    return sum(counts)