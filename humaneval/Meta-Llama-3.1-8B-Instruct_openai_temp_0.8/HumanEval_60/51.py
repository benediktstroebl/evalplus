### Sum of Numbers from 1 to n

The following Python script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n`.

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
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    return n * (n + 1) // 2

# Example usage
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1

```

This code uses the arithmetic series formula `n * (n + 1) / 2` to efficiently calculate the sum of numbers from 1 to `n`. The function also includes input validation to ensure that `n` is a positive integer.