```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start checking from the largest possible divisor (n-1)
    # We only need to check up to the square root of n because a larger factor of the number would be a multiple of a smaller factor that has already been checked.
    for i in range(min(n-1, int(n**0.5)), 0, -1):
        if n % i == 0:
            return i
    # If no divisor is found (which is highly unlikely), return 1
    return 1

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(24))  # Expected output: 12
```

This script defines a function `largest_divisor(n)` that finds the largest divisor of a given number `n`, which is smaller than `n`. It starts checking from the largest possible divisor (n-1) down to 1 and returns the first divisor it finds. If no divisor is found, it returns 1. The `min(n-1, int(n**0.5))` expression is used to optimize the loop by only checking up to the square root of `n`.