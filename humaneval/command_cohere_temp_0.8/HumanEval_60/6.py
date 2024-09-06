```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): The highest number to be included in the sum.

    Returns:
        int: The sum of integers from 1 to n (inclusive).
    """
    return n * (n + 1) // 2  # Sum formula for pairs of integers

# Test cases
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

The function utilizes the sum formula for pairs of consecutive integers: `n(n+1) / 2`, which simplifies to `n^2 + n / 2`. This formula is intuitive as the sum of adjacent integers, including the sum of `n` itself, is the total for the range from 1 to `n`.