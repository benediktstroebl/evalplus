```python
def sum_to_n(n: int):
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
    return sum(range(1, n + 1))


# Test cases
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

This script defines a function `sum_to_n` that uses the built-in `sum` function along with the `range` function to calculate the sum of numbers from 1 to n. The `range` function generates a sequence of numbers from 1 to n (exclusive of n), and the `sum` function adds up all these numbers. The script then tests the `sum_to_n` function with the provided test cases.