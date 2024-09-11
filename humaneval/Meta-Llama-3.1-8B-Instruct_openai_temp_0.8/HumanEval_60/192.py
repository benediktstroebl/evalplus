### Sum to N Function

The following Python script defines a function `sum_to_n` that calculates the sum of numbers from 1 to n.

```python
def sum_to_n(n: int) -> int:
    """
    Calculate the sum of numbers from 1 to n.

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
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    
    return sum(range(1, n + 1))

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script uses the built-in Python function `sum` in combination with the `range` function to calculate the sum of numbers from 1 to n. It also includes error checking to ensure that the input is a positive integer.