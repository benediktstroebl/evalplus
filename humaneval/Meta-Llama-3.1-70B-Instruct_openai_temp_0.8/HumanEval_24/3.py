```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    >>> largest_divisor(15)
    5
    >>> largest_divisor(17)
    1
    """
    # Start checking from n-1 down to 1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it immediately
            return i
    # If no divisors are found, return 1 (since 1 is a divisor of all numbers)
    return 1


# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(17))  # Should print 1
```

This script defines the `largest_divisor` function, which iterates down from `n-1` to find the largest number that divides `n` evenly. The function includes docstrings and type hints for clarity, and it includes test cases to verify the function's correctness.