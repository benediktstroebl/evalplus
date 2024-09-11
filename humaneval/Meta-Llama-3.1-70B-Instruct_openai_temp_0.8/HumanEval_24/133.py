```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(48))  # Expected output: 24
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function works by iterating over the numbers from `n-1` to 1 in reverse order and checking if each number is a divisor of `n`. The first number that is a divisor is returned as the largest divisor. If no divisors are found, the function returns `None`.