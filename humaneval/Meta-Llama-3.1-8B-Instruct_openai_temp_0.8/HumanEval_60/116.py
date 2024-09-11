### Python Script to Sum Numbers from 1 to n

```python
def sum_to_n(n: int):
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
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    return n * (n + 1) // 2

# Example usage:
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines the `sum_to_n` function, which uses the arithmetic series formula to efficiently calculate the sum of numbers from 1 to `n`. The function also includes input validation to ensure that `n` is a positive integer.

Note: The formula `n * (n + 1) // 2` works because the sum of an arithmetic series with `n` terms, where the first term is `a` and the last term is `l`, is given by `n * (a + l) // 2`. In this case, `a = 1` and `l = n`, so the formula simplifies to `n * (1 + n) // 2`, which is equivalent to `n * (n + 1) // 2`.