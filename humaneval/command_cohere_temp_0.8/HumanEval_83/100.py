```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit positive integer
    counts = [0] * (n * 10)
    
    # Count the numbers that start with 1
    for i in range(1, n + 1):
        counts[1000 * (i - 1) + 1] += 1
    
    # Count the numbers that end with 1
    for i in range(1, n + 1):
        counts[1000 * i + 1] += 1
    
    return sumsolve(counts, n)

def sumsolve(array, n):
    total = 0
    for i in range(0, n):
        total += array[i]
    return total
```

This Python code defines a function `starts_one_ends` that takes an integer `n` as input and counts the number of `n-digit` positive integers that start or end with the digit 1. It accomplishes this by creating a `counts` array filled with zeros, then populating it with the count of numbers starting or ending with 1 for each possible `n-digit` positive integer. The final count is computed within the `sumsolve` function and returned as the result, with comments explaining each step of the process.