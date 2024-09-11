```python
# sum_to_n.py
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit for the sum.

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
    # Using the formula for the sum of arithmetic series: n*(n+1)/2
    return n * (n + 1) // 2

# Test the function
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script defines the `sum_to_n` function using the mathematical formula for the sum of an arithmetic series, which makes it efficient for large values of `n`. The `doctest` module is used to automatically test the function with the provided examples.