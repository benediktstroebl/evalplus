def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit positive integer
    counts = [0] * (n * 10)
    
    # Count the numbers that start with 1
    for i in range(1, n + 1):
        counts[1000 * (i - 1) + 1] += 1
    
    # Count the numbers that end with 1
    for i in range(1, n + 1):
        counts[1000 * i + 1] += 1
    
    return sumsolve(counts, n)
def sumsolve(array, n):
    total = 0
    for i in range(0, n):
        total += array[i]
    return total