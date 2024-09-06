def starts_one_ends(n):
    # Create a list to store the counts of starting or ending with 1
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += 1
    
    return sumsolve(counts, n)
def sumsolve(counts, target):
    # Convert counts to sums (can be computed in linear time)
    sums = [sum(counts[i:i+target]) for i in range(0, target + 1)]
    
    # Remove duplicates (to count the occurrences)
    temp = []
    for i in range(len(sums)):
        if sums[i] not in temp:
            temp.append(sums[i])
    sums = temp
    
    return sums