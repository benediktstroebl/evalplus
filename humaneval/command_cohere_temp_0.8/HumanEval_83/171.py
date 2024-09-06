Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the markdown code block:
```python
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
    totals = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == n:
            totals[i] = 1
        else:
            totals[i] = totals[i + 1] + totals[i - 1]
    
    return counts[1] + totals[n]
```

This function calculates the count of numbers that start or end with 1 within n-digit positive integers using a combination of dynamic programming and mathematical reasoning. It is indeed a self-contained solution within the specified code block.