```python
# Simple Python script that calculates the sum of numbers from 1 to n

def sum_to_n(n: int) -> int:
    """
    Calculates the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

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
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

This script uses the formula for the sum of an arithmetic series, `n * (n + 1) / 2`, to calculate the sum of numbers from 1 to n. This is more efficient than using a loop to add up the numbers one by one. The script includes docstrings to provide a description of the function, its arguments, and its return value, as well as some examples of how to use it.