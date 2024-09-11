```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
    """
    return (n * (n + 1)) // 2

# Test the function
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

This script defines a function `sum_to_n` that uses the formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to `n`. The formula is `(n * (n + 1)) // 2`, where `n` is the upper limit of the range. This formula is more efficient than calculating the sum using a loop, especially for larger values of `n`. The script also includes docstrings to provide documentation for the function and test cases to verify its correctness.