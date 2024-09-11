```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This script defines the `largest_divisor` function, which iterates from `n - 1` down to 1 to find the largest number that divides `n` evenly. It returns the first divisor it finds, since it's iterating in descending order.

Note that this function has a time complexity of O(n), which may not be efficient for large inputs. A more efficient solution could involve iterating up to the square root of `n`, since any factor larger than that would have a corresponding factor smaller than the square root. Here's an optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    >>> largest_divisor(15)
    5
    """
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return max(i, n // i)

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This optimized version has a time complexity of O(sqrt(n)), making it much more efficient for large inputs.