```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(10)
    5
    >>> largest_divisor(17)
    1
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(10))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
```
This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating over the numbers from `n - 1` down to 1, and returning the first number that divides `n` without leaving a remainder.

However, we can improve this function by only checking numbers up to the square root of `n`, because a larger factor of `n` would be a multiple of a smaller factor that has already been checked.

Here is the improved version:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(10)
    5
    >>> largest_divisor(17)
    1
    """
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return max(i, n // i)
    return 1

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(10))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
```
This version of the function is more efficient for large inputs, because it only checks numbers up to the square root of `n`, rather than all the way down to 1.