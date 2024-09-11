```python
def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.

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

This Python script defines a function called `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the mathematical formula `n * (n + 1) / 2` to calculate the sum, making it efficient even for large values of `n`. The script also includes a docstring that documents the function's behavior and provides examples of how to use it.