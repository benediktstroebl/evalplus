```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

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
    # Check if n is an integer
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    
    # Check if n is a non-negative integer
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    return n * (n + 1) // 2
```
This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function first checks if `n` is a non-negative integer, and raises a `TypeError` or `ValueError` if not. It then uses the formula for the sum of an arithmetic series to calculate the sum efficiently. The docstring provides a description of the function, its arguments, and its return value, as well as some example use cases.