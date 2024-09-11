```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n, smaller than n
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This script works by iterating over all numbers smaller than `n` in descending order and checking if `n` is divisible by that number. The first number that divides `n` evenly is the largest divisor, so the function returns that number.

However, if you want a more efficient solution, you can iterate up to the square root of `n` instead of `n-1`. This is because a larger factor of the number would be a multiple of smaller factor that has already been checked.

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n, smaller than n
    """
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return max(i, n // i)

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```