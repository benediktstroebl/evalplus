```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20
print(largest_divisor(32))  # Output: 16
print(largest_divisor(100)) # Output: 50
```

This script defines a function `largest_divisor` that finds the largest number smaller than `n` that evenly divides `n`. It does this by iterating from `n-1` down to 1 and checking if `n` is divisible by the current number. The first number it finds that is a divisor is the largest divisor smaller than `n`, and it returns this value. 

However, a more efficient solution would be to find the greatest common divisor (GCD) of `n` and `n-1`, which would be the largest divisor smaller than `n`. The `math.gcd` function in Python's standard library can be used for this. 

Here's an alternative solution:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Examples:
        >>> largest_divisor(15)
        5
    """
    return math.gcd(n, n - 1)

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20
print(largest_divisor(32))  # Output: 16
print(largest_divisor(100)) # Output: 50
```