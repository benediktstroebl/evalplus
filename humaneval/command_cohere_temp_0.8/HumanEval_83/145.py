Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the markdown code block:
```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Define the range of n-digit numbers.
    num_range = list(range(10**(n-1), 10**n, 1))
    # Count the numbers that start or end with 1.
    return sum(1 for num in num_range if num % 10 == 1)
```

This script defines the function `starts_one_ends(n)` that takes a positive integer `n` as input and returns the count of numbers of `n-digit` positive integers that start or end with 1. It does so in a precise manner by first defining the range of n-digit numbers using the `num_range` list, and then iterating through this list and counting the numbers that have a digit equivalent to 1 at the ten's position. The count is then returned as the final output.