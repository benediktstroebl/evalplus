### Sum of Numbers from 1 to n

Here is a Python function that calculates the sum of numbers from 1 to n using the formula `n * (n + 1) / 2`:

```python
def sum_to_n(n: int) -> int:
    """
    Sum of numbers from 1 to n.

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
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 1:
        raise ValueError("Input must be a positive integer.")

    return n * (n + 1) // 2
```

This function takes an integer `n` as input, checks if it's a positive integer, and returns the sum of numbers from 1 to `n` using the formula `n * (n + 1) / 2`. The `//` operator is used for integer division to ensure the result is an integer.

You can test this function with different inputs to see the sum of numbers from 1 to `n`.