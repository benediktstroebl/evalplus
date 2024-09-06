```python
def starts_one_ends(n):
    # Create a list to store the results for bases from 1 to n
    result = [0] * (n + 1)
    
    # Count the numbers that start with 1
    result[1] = 1
    
    # Count the numbers that end with 1
    half_n = n // 2
    for base in range(2, half_n + 1):
        result[base] += result[base - 1]
    
    # Adjust the count for numbers that start and end with 1
    result[1] -= result[0]
    result[n] -= result[n - 1]
    
    return result[n]
```

This script provides a function `starts_one_ends(n)` that takes in a positive integer `n` and returns the count of `n-digit` positive integers that start or end with 1. The approach is to generate an arithmetic series within the range of bases from 1 to `n`, and then adjust the counts for numbers that start and end with 1, hence the -1 indexing.