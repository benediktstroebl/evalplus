```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

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
    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    return n * (n + 1) // 2

# Test the function with the provided examples
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))    # 15
print(sum_to_n(10))   # 55
print(sum_to_n(1))    # 1
```

This script defines the `sum_to_n` function using the mathematical formula for the sum of an arithmetic series, which is more efficient than iterating over the numbers from 1 to n. The example tests demonstrate the function's correctness.