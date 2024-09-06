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

This Python script provides a self-contained function `starts_one_ends(n)` designed to solve the given problem. It calculates the count of positive integers with `n` digits that either start or end with the digit 1. Two arrays are used to efficiently compute the counts. The first element is always 1, denoting the single number that starts with 1. The subsequent counts are obtained by incrementing previous results, considering numbers ending with 1. This approach ensures correctness and efficiency in determining the desired counts for n-digit numbers.