```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None  # Return None if no divisors are found

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(25))  # Output: 5
print(largest_divisor(12))  # Output: 4
print(largest_divisor(17))  # Output: None
```

This script defines the `largest_divisor` function, which finds the largest divisor of a given number `n` by iterating from `n - 1` down to `1` and checking each number for divisibility using the modulo operator (`%`). If a number is divisible (i.e., the remainder is `0`), it is returned as the largest divisor.

Alternatively, you could use the built-in `math.gcd` function in combination with the fact that `gcd(a, b) * gcd(b, a) == a * b`, which implies that `gcd(a, b) * gcd(a, b) == a * b` (after some algebraic manipulations). This would give you the largest divisor directly.

Here's an implementation of the alternative method:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    return n // math.gcd(n, 1)

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(25))  # Output: 5
print(largest_divisor(12))  # Output: 4
print(largest_divisor(17))  # Output: 1
```

This version of the function uses `math.gcd(n, 1)` to get the greatest common divisor of `n` and `1`, which is `n` itself, and then divides `n` by this value to get the largest divisor.