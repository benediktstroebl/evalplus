Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the markdown code block:
```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a count array to store the counts of numbers starting or ending with 1 for each length
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[-1]
```

This script creates an array `counts` where each element `counts[i]` represents the count of n-digit positive integers that start or end with 1, for `n = i`-digit numbers. It then iterates through the lengths of numbers from 2 to `n` and updates the `counts` array such that `counts[i]` represents the count of (`i`-digit) numbers that start with 1, and the sum of `counts` from length 2 to `n` represents the count of (`n`-digit) numbers that end with 1. The final count is then returned.