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
        raise ValueError("Input must be a positive integer.")
    return sum(range(1, n + 1))

# Test the function
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))  # 15
print(sum_to_n(10))  # 55
print(sum_to_n(1))  # 1
```

This script defines the `sum_to_n` function, which takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the built-in `sum` function and the `range` function to generate the numbers to be summed. It also includes a docstring with examples and a test at the end to verify that the function works correctly.