```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor of.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Outputs: 5
```
This script defines a function `largest_divisor` that iterates over all numbers smaller than `n` in descending order, checking if `n` is divisible by each one. The first number it finds that divides `n` evenly is the largest divisor, so it returns that number.

Note that this solution has a time complexity of O(n), which means it may not be efficient for large inputs. A more efficient solution can be achieved by iterating only up to the square root of `n`, like this:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor of.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return max(i, n // i)

# Example usage:
print(largest_divisor(15))  # Outputs: 5
```
This version of the function has a time complexity of O(sqrt(n)), making it much more efficient for large inputs.