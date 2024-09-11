```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number for which to find the largest divisor.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Raises:
        ValueError: If n is less than 1.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(10)
        5
        >>> largest_divisor(13)
        1
    """
    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Start checking from n-1 down to 1
    for i in range(n - 1, 0, -1):
        # If i is a divisor of n, return it
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(13))  # Output: 1
```

This script defines the function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple iterative approach to check all numbers from `n-1` down to `1` to see if they are divisors of `n`. As soon as it finds a divisor, it returns that number. If no divisors are found (which would be the case for prime numbers), the function returns `1`, since `1` is a divisor of every number.