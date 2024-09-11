```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
        n (int): The upper limit for the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Example:
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
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the formula `n * (n + 1) / 2` to calculate the sum, which is more efficient than using a loop.

The script also includes docstrings to provide documentation for the function, and example use cases to demonstrate its usage. Additionally, it includes input validation to ensure that the input is a positive integer.