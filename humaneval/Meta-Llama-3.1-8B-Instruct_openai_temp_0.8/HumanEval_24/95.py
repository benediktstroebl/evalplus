```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n smaller than n.

    Example:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1  # If no divisors are found, return 1

# Test the function
print(largest_divisor(15))  # Expected output: 5
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It iterates over the numbers from `n-1` down to 1, checking each number to see if it's a divisor of `n` by using the modulo operator (`%`). If it finds a divisor, it returns that divisor. If it doesn't find any divisors, it returns 1.