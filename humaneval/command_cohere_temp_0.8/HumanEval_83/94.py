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

This Python script defines a function `starts_one_ends(n)` to count the numbers of `n-digit` positive integers that start or end with 1. The solution proceeds by creating a list `counts` to store the results, initially setting `counts[1]` to 1 to account for the single starting number 1. Then, for each number from 2 to n, it increments the count in the `counts` list for the current number and also accounts for numbers that end with 1 by incrementing the count for the current number based on the count of numbers ending with 1 from the previous digit length. Finally, it returns `counts[n]`, which represents the desired count of numbers that start or end with 1 within `n-digit` positive integers.