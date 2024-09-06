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

This approach uses a cyclical convolution to count the numbers that end with 1. The function iterates through the digits from 2 to n, and for each digit, it adds the count of the previous digit to itself. This is done because to count the numbers that end with 1, you'd increment the count of n-digit numbers by the count of (n-1)-digit numbers. This approach avoids the need to iterate through all (n-1)-digit numbers, making it more efficient.