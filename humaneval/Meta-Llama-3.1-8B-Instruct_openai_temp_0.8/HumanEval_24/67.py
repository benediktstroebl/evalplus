```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest number that divides n evenly.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
```

In this script, we define a function `largest_divisor` that takes an integer `n` as input. The function iterates from `n-1` down to `1`, checking each number to see if it divides `n` evenly (i.e., if `n` is divisible by the current number). As soon as it finds a number that does divide `n`, it returns that number. This ensures that the function returns the largest number that divides `n` evenly, smaller than `n`.