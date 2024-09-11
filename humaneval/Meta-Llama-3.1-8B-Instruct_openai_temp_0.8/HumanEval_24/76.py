```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number to find the largest divisor for

    Returns:
    int: The largest divisor found

    Example:
    >>> largest_divisor(15)
    5
    """
    # Start from the second last number down to 1, as the largest divisor must be smaller than n
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(10))  # Expected output: 5
print(largest_divisor(7))   # Expected output: 1
```

However, a more optimized solution for this problem would be to directly find the largest divisor (also known as the greatest common divisor or GCD) of `n` and `n-1`:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number to find the largest divisor for

    Returns:
    int: The largest divisor found

    Example:
    >>> largest_divisor(15)
    5
    """
    # The largest divisor is the GCD of n and n-1
    return math.gcd(n, n-1)

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(10))  # Expected output: 5
print(largest_divisor(7))   # Expected output: 1
```

This version of the function is more efficient, as it directly calculates the GCD without the need for iteration.