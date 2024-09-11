```python
def sum_to_n(n: int):
    """
    Sum numbers from 1 to n.

    Args:
        n (int): The upper limit.

    Returns:
        int: The sum of numbers from 1 to n.

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
    if n < 1:
        return "Input should be a positive integer"
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))   # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
print(sum_to_n(0))    # Output: Input should be a positive integer
```

This script includes a docstring to describe the function's purpose and behavior, and also includes a check to handle cases where the input `n` is less than 1. The function's calculation is based on the formula for the sum of an arithmetic series.