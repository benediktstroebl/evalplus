```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(12)
    4
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 4
```

This script defines the `largest_divisor` function that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating from `n - 1` down to `1` and checking if each number is a divisor of `n` using the modulo operator (`%`). If it finds a divisor, it returns that number. If it doesn't find any divisors (which shouldn't happen for positive integers), it returns `None`. The example use cases are provided using doctests.