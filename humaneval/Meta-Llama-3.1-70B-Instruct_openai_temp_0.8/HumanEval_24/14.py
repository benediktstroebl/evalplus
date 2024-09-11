```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly, smaller than `n`. It does this by iterating from `n-1` down to `1` and checking for divisibility. The function returns the first number it finds that divides `n` evenly, which will be the largest divisor.

Alternatively, you can use a more efficient approach by iterating up to the square root of `n`:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return max(i, n // i)

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This version of the function uses the `math.sqrt` function to calculate the square root of `n` and then iterates from there down to `1`. This reduces the number of iterations and makes the function more efficient for large values of `n`.