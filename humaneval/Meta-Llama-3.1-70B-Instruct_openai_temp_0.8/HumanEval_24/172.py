```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Raises:
        ValueError: If n is less than 2.

    Examples:
        >>> largest_divisor(15)
        5
    """
    if n < 2:
        raise ValueError("Input number should be greater than or equal to 2")

    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```

This script works by iterating over numbers from `n - 1` down to `1` and checking if `n` is divisible by the current number. As soon as it finds a divisor, it returns that number, which is the largest divisor smaller than `n`.

Alternatively, you can use a more efficient approach by only iterating up to the square root of `n`, since a larger factor of `n` would be a multiple of a smaller factor that has already been checked:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Raises:
        ValueError: If n is less than 2.

    Examples:
        >>> largest_divisor(15)
        5
    """
    if n < 2:
        raise ValueError("Input number should be greater than or equal to 2")

    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return max(i, n // i)

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```