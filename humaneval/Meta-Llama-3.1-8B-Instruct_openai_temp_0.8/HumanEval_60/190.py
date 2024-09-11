### Calculating Sum of Numbers from 1 to n
```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the range.

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

# Test the function with the provided examples
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```
This script uses the formula for the sum of an arithmetic series: `n * (n + 1) / 2`, where `n` is the upper limit of the range. The `//` operator is used for integer division to ensure the result is an integer.