```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Example:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and go down, checking each number if it's a divisor of n
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i
    # If no divisor is found, return 1 (1 is a divisor of every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(25))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n-1` down to `1`, checking each number if it's a divisor of `n`. If a divisor is found, it's immediately returned. If no divisor is found, the function returns `1`, since `1` is a divisor of every number. The function is then tested with a few examples.