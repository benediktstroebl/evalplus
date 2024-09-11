**Sum of Numbers from 1 to n**
================================

Here's a simple Python function that uses the mathematical formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to `n`.

```python
def sum_to_n(n: int) -> int:
    """
    Sum of numbers from 1 to n.

    Args:
    n (int): The last number in the series.

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
    if n < 1:
        raise ValueError("n must be a positive integer")
    return (n * (n + 1)) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script uses the formula `n * (n + 1) / 2` to calculate the sum of numbers from 1 to `n`. This formula is derived from the formula for the sum of an arithmetic series, which is `n/2 * (a1 + an)`, where `n` is the number of terms, `a1` is the first term, and `an` is the last term. In this case, `a1` is always 1, and `an` is `n`.