```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the range of numbers.

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
    # Using the formula for the sum of an arithmetic series: n * (n + 1) / 2
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines the `sum_to_n` function, which uses the formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to `n`. The script also includes test cases at the end to verify the correctness of the function. The `//` operator is used for integer division to ensure the result is an integer.