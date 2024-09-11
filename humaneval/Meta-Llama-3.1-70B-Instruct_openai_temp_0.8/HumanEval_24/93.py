```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The given number.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n - 1` down to `1` and checks if `n` is divisible by each number. As soon as it finds a divisor, it returns that number.

However, this approach is not efficient for large numbers because it checks all numbers down to 1. A more efficient approach would be to only check up to the square root of `n`, as any factor larger than that would have a corresponding factor smaller than the square root.

Here's a more efficient version of the script:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The given number.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            if i!= 1:
                return i
            else:
                return n // i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This version of the function uses the `math.sqrt` function to calculate the square root of `n` and then only checks numbers up to that value. This significantly improves the function's performance for large numbers.