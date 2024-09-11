```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Start from the largest possible divisor, which is n-1
    for i in range(n-1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(25))  # Output: 5
print(largest_divisor(30))  # Output: 15
```

This script defines a function `largest_divisor` that iterates from `n-1` down to 1 to find the largest number that divides `n` evenly. The function uses the modulo operator `%` to check for divisibility. If `n` is divisible by a number `i`, the function returns `i`. If no such number is found, the function will implicitly return `None`. However, based on the problem statement, it is guaranteed that such a number exists for any positive integer `n`.