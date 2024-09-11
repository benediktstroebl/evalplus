```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
    n (int): A positive integer.

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
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")

    # Using the mathematical formula for the sum of an arithmetic series
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n(n)` that calculates the sum of numbers from 1 to `n` using the mathematical formula for the sum of an arithmetic series. It also includes a docstring that provides information about the function's parameters, return value, and examples of usage. Additionally, it includes a test section that demonstrates the function's output for various inputs.