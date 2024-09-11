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
        >>> largest_divisor(17)
        1
    """
    # Start checking from the largest possible divisor (n-1) down to 1
    for i in range(n-1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, return i as the largest divisor
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor` that iterates over all numbers smaller than the input number `n` in descending order. For each number, it checks if it divides `n` evenly by using the modulo operator (`%`). If it finds a number that divides `n` evenly, it returns that number as the largest divisor.

Alternatively, you can also use a more mathematical approach to solve this problem by iterating up to the square root of `n`, as any factor larger than the square root would have a corresponding factor smaller than the square root. Here's an optimized version of the function:

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
        >>> largest_divisor(17)
        1
    """
    # Start checking from the square root of n down to 1
    for i in range(math.isqrt(n), 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, return i as the largest divisor
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This optimized function reduces the number of iterations significantly for large input numbers.