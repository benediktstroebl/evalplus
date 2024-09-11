```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n that is smaller than n

    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start checking from the largest possible divisor, which is n-1
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it immediately
            return i

# Test the function
print(largest_divisor(15))  # Should print 5
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest divisor of `n` that is smaller than `n`. The function works by checking all numbers from `n-1` down to 1 to see if they are divisors of `n`. As soon as it finds a divisor, it returns that divisor. The script also includes a test case to verify that the function works correctly.