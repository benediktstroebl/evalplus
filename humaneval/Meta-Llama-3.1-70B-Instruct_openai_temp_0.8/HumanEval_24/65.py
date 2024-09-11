```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor of.

    Returns:
    int: The largest divisor of n, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check if it's a divisor of n
    for i in range(n-1, 0, -1):
        # If n is divisible by i, it's a divisor
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines the `largest_divisor` function, which takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by checking all numbers from `n-1` down to `1` to see if they are divisors of `n`. The first number it finds that is a divisor is the largest divisor of `n`, so it returns that number.