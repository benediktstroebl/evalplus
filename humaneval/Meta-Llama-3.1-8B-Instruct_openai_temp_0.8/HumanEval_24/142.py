```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number for which to find the largest divisor.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the number n-1 and decrement until we find a divisor
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i
            return i
    # If no divisor is found, return 1 (since 1 is a divisor of all numbers)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor(n)` that finds the largest number `i` that divides `n` evenly and returns it. The function starts from `n-1` and decrements until it finds a divisor, then returns that divisor. If no divisor is found, the function returns 1. The script includes example usage and documentation for the function.