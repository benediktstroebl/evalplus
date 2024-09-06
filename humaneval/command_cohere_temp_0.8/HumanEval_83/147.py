```python
def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[n]
```

This Python script provides a self-contained function `starts_one_ends(n)` designed to calculate the count of positive integers that are `n` digits long and either start or end with the digit 1. The solution is based on an intuitive approach that involves counting the numbers that end with 1, which can then be augmented to account for those that start with 1. The function returns the count of such numbers, providing a efficient and concise solution.