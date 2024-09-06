def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes the starting zeros.
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += 1
    
    return sumsolve(counts)
def solve(a, b):
    if b == 0:
        return a
    else:
        return a + solve(b, b - 1)
def sumsolve(count):
    return solve(count[0], count[1:])