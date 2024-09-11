```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```

This script defines a function `largest_divisor` that finds the largest divisor of `n` smaller than `n` by iterating through all numbers in descending order and checking for divisibility. The first divisor found will be the largest one smaller than `n`.