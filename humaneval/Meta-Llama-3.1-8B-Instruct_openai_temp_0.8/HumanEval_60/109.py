```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.

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
```

This function uses the formula for the sum of an arithmetic series to calculate the sum directly, without having to iterate over all numbers from 1 to n. This makes it more efficient, especially for large values of n.