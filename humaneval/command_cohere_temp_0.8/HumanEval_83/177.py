```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[n]
```

This approach uses a clever accumulation technique to count the numbers that end with 1. For each number from 2 to n, you increment the count of numbers that end with 1 by adding the count of numbers that end with 01 to the count of numbers that end with 11, 101, 111, and so on.

The counts array is initialized with zeros so that you don't have to worry about initial values for numbers less than 2. The count for n = 1 is explicitly set to 1 since there is one number (11) that starts or ends with 1 in a 1-digit number.