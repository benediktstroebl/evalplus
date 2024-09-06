```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[-1]
```

This approach uses a somewhat intuitive method, where we calculate the counts of numbers that end with 1 by propagating the counts of smaller numbers that end with 1. We also account for the single number that starts with 1. Finally, the `counts` list is returned, which contains the count of numbers that end with 1 for each possible `n-digit` number.