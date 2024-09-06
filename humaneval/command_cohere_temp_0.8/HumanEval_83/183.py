Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the prompt:
```python
def starts_one_ends(n):
    # Create a list to store the results of subproblems
    counts = [0] * (n + 1)
    
    # Count numbers that start with 1
    counts[1] = 1
    
    # Count numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[-1]
```

This script provides a direct approach to solving the problem by creating a 1-based range from 1 to n and iterating from 2 to n-1, incrementing the count of numbers ending in 1 for each iteration. The final count of numbers ending in 1 is then returned.