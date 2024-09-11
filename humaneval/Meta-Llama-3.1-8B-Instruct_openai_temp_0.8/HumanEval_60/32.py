### Summing Numbers from 1 to N

The following Python script defines a function `sum_to_n` that calculates the sum of numbers from 1 to n.

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
    if n < 1:
        raise ValueError("Input should be a positive integer.")
    return n * (n + 1) // 2

# Example usage:
print(sum_to_n(30))   # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

This script utilizes the formula for the sum of an arithmetic series, `n * (n + 1) / 2`, to calculate the sum in O(1) time complexity. The function `sum_to_n` first checks if the input `n` is less than 1 and raises a `ValueError` if it is. Otherwise, it returns the calculated sum.