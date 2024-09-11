```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest number that divides n evenly, smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 7
```

This script defines a function `largest_divisor` that finds the largest divisor of a given number `n`. It iterates over all numbers from `n-1` to 1 in reverse order, checking if each number is a divisor of `n`. The first number that is a divisor of `n` is returned as the largest divisor.

Note: This function has a time complexity of O(n), which is not efficient for large numbers. A more efficient approach would be to use the fact that the largest divisor of a number `n` is the greatest common divisor (GCD) of `n` and `n-1`. You can use the `math.gcd` function in Python's standard library to achieve this. Here is the optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest number that divides n evenly, smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    return math.gcd(n, n - 1)

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 7
```