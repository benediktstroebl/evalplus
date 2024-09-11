```python
def sum_to_n(n: int):
    """
    This function calculates the sum of all numbers from 1 to n.

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
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

In this script, the `sum_to_n` function uses the formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to `n`. The formula is `n * (n + 1) / 2`. This formula is more efficient than calculating the sum by iterating over all numbers from 1 to `n`, especially for large values of `n`.