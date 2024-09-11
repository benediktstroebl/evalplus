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
    # start checking from the largest possible divisor, which is n // 2
    for i in range(n // 2, 0, -1):
        # if n is divisible by i, return i
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This script defines the `largest_divisor` function, which takes an integer `n` as input and returns its largest divisor smaller than `n`. The function iterates from `n // 2` down to 1 and returns the first number that divides `n` evenly. If no such number is found, the function implicitly returns `None`, but in this case, we know that every number has at least one divisor (1), so this shouldn't be an issue.