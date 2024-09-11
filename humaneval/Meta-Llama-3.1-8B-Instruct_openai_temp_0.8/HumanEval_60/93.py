```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

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
    return sum(range(1, n + 1))
```

In this script, we define the `sum_to_n` function which takes an integer `n` as input and returns the sum of all integers from 1 to `n`. The `range` function generates a sequence of numbers starting from 1 up to, but not including, `n`. The `sum` function adds up all these numbers. The function also includes docstrings that describe its purpose, parameters, return value, and provide some examples of its usage. 

This solution is simple, efficient, and easy to understand, making it a good choice for this problem.