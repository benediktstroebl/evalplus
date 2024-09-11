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
    return sum(range(1, n + 1))


# Test the function
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

This script uses the built-in `sum` function in Python, which calculates the sum of all elements in a sequence. The `range(1, n + 1)` function generates a sequence of numbers from 1 to n. The `sum_to_n` function takes an integer `n` as input, calculates the sum of numbers from 1 to n, and returns the result. The final part of the script tests the `sum_to_n` function with the provided examples.