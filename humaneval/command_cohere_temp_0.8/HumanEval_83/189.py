```python
def starts_one_ends(n):
    # Create a list to store the results for  1st and last position
    counts = [0 for i in range(n+1)]
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Calculate counts of numbers that end with 1
    for i in range(2, n+1):
        counts[i] += counts[i-1]
    
    return counts[-1]
```

This Python script provides a self-contained function `starts_one_ends(n)` designed to solve the given problem. It calculates the count of positive integers with `n` digits that either start or end with the digit 1. It iterates through numbers from 2 to `n` and maintains a count of numbers ending with 1 by updating the counts list. The final count is returned, representing the count of `n-digit` positive integers that start or end with 1.