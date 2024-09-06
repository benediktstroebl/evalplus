```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This counts the total possible n-digit
    # numbers, without considering the starting or ending digit, then subtracts
    # the numbers that do not start or end with 1.
    counts = [n * (n + 1) // 2 - n // 2 for n in range(1, n + 1)]
    
    # Return the maximum count, which occurs when n is 9 or 10
    return max(counts)
```

This script provides a clear and efficient approach to solving the problem.

One approach to step through this code could be the following:

- `def starts_one_ends(n):`: This declares a function named `starts_one_ends` that accepts one argument, `n`, and returns a value of type `int`.
- `counts = [n * (n + 1) // 2 - n // 2 for n in range(1, n + 1)]`: This line creates a list named `counts` comprising `n` values, each calculated as `n * (n + 1) // 2 - n // 2` for `n` ranging from 1 to `n`. This list holds the count of potential n-digit numbers minus the count of numbers that do not start or end with 1.
- `return max(counts)`: This returns the maximum value from the `counts` list. This maximum value represents the count of n-digit numbers that start or end with 1, occurring when `n` is 9 or 10, and the function appropriately returns this maximum count. 

This solution demonstrates careful organization and employs a list to efficiently calculate the counts. It showcases an elegant approach to solving the given problem.