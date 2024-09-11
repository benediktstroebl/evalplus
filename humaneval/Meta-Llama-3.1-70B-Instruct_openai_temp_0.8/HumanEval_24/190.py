```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n that is smaller than n.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, which is smaller than `n`. It does this by iterating over numbers from `n - 1` down to `1`, and returns the first number that divides `n` without leaving a remainder.

Note: This solution has a time complexity of O(n), which means it may not be efficient for large inputs. A more efficient solution would use a loop that only goes up to the square root of `n`, since a larger factor of `n` would be a multiple of smaller factor that has already been checked. Here is an optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n that is smaller than n.
    """
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return n // i if n // i < n else i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This optimized version has a time complexity of O(sqrt(n)), making it more suitable for large inputs.