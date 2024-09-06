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

This approach uses a cyclical convolution to count the numbers that end with 1. The variable `counts` is initialized with the count of numbers that start with 1 (there's only one such number - namely, '1'). Then, the loop iterates from 2 to n, where each number is represented by `i`. The previous count of ending in 1 is subtracted from the current count to eliminate double-counting. Finally, the total count of numbers ending in 1 is returned, which is `counts[n]`.