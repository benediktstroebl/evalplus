```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n using the formula for the sum of an arithmetic series.

    Args:
        n (int): The upper limit of the series.

    Returns:
        int: The sum of the series from 1 to n.

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
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```
This script defines the function `sum_to_n` that calculates the sum of the numbers from 1 to `n` using the formula for the sum of an arithmetic series: `n * (n + 1) / 2`. The function is then tested with the provided example cases.