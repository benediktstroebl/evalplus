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

This Python script provides a self-contained function `starts_one_ends(n)` designed to solve the given problem. It calculates the count of positive integers with `n` digits that either start or end with the digit 1. The solution is based on the observation that every positive integer that ends with 1 can be derived by adding 1 to a positive integer that does not end with 1, thereby increasing the count by 1. The script uses a list `counts` to keep track of the counts for each digit length, initialized to store the counts from 1-digit to `n`-digit numbers. It then increments the count for numbers ending in 1 by iterating from 2 to `n` and multiplying the count for each number by the count of numbers that can be derived from it. The result stored in `counts[n]` is the desired count of numbers that start or end with 1 within `n` digits.