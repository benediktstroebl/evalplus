
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    
    # Store counts of digits = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 2, 8: 2, 9: 3}
    counts = {}
    for i in range(len(str(n))):
        counts[i+1] = counts.get(i+1, 0) + 1
    
    # Count of 5-digit positive integers that start with 1
    count = counts.get(5, 0)
    
    # Count of 5-digit positive integers that end with 1
    count += counts.get(6, 0)
    
    # Count of 5-digit positive integers that start or end with 1
    count += sum(counts.values()) - counts.get(7, 0) - counts.get(8, 0) - counts.get(9, 0)
    
    return count

