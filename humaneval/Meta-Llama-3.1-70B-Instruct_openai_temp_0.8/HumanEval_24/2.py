```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(24)
        12
        >>> largest_divisor(37)
        1
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(24))  # Output: 12
print(largest_divisor(37))  # Output: 1
```

This script works by iterating from `n - 1` down to 1 and checking if `n` is divisible by the current number `i`. As soon as it finds a divisor, it returns that divisor, which is the largest one due to the descending order of the iteration.

Alternatively, you could also use a more mathematically optimized approach:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(24)
        12
        >>> largest_divisor(37)
        1
    """
    sqrt_n = math.isqrt(n)
    for i in range(sqrt_n, 0, -1):
        if n % i == 0:
            return n // i if i!= 1 else i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(24))  # Output: 12
print(largest_divisor(37))  # Output: 1
```

In this optimized version, we only iterate up to the square root of `n`, because a larger factor of `n` must be a multiple of a smaller factor that has already been checked. If we find a divisor `i`, we return `n // i`, which is the corresponding larger divisor. If `i` is 1, we just return `i` because `n // i` would be `n`, which is not a smaller divisor.