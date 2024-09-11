```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(10)
    5
    >>> largest_divisor(7)
    1
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```

This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly, smaller than `n`. It does this by iterating over the numbers from `n-1` down to 1 and checking if each number is a divisor of `n`. The first number it finds that is a divisor is returned as the result. If no divisors are found (which is the case for prime numbers), the function returns 1. 

The script then tests the function with some examples to verify that it works as expected.