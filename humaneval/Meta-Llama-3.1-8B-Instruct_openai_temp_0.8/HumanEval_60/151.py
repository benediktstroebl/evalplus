### Sum of Numbers from 1 to n

Here is a Python function that sums numbers from 1 to n using a simple arithmetic formula.

```python
def sum_to_n(n: int) -> int:
    """
    Sums numbers from 1 to n.

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


# Test cases
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))  # 15
print(sum_to_n(10))  # 55
print(sum_to_n(1))  # 1
```

This function uses the formula for the sum of an arithmetic series: `n * (n + 1) / 2`, which is more efficient than summing all the numbers from 1 to n.

However, this code includes error checking to ensure that the input is a positive integer. If not, it raises a TypeError or ValueError respectively.