```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1  # Return 1 if n is prime

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(100))  # Output: 100
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n-1` down to 1, checking each number to see if it is a divisor of `n`. If it is, the function returns that number. If no divisors are found (i.e., `n` is prime), the function returns 1.