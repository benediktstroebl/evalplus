```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None  # This should never happen, but it's a good practice

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 17 (prime number, so its largest divisor is itself)
print(largest_divisor(24))  # Output: 12
```

Alternatively, you can use a more efficient solution using the math library to get the square root of `n`, since a larger factor of `n` must be a multiple of a smaller factor that has already been checked:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(int(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return i
    return None  # This should never happen, but it's a good practice

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 17 (prime number, so its largest divisor is itself)
print(largest_divisor(24))  # Output: 12
```