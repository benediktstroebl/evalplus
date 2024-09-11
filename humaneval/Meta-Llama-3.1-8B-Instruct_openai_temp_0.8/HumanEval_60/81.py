Here's a self-contained Python script that solves the problem:
```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The number up to which the sum should be calculated.

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
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```
This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the formula for the sum of an arithmetic series, which is `n * (n + 1) // 2`, to calculate the sum in O(1) time. The function also includes input validation to raise a `ValueError` if `n` is not a positive integer. The script then tests the function with the provided examples.