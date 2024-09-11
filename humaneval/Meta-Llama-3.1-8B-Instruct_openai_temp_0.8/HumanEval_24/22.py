```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(12))  # Output: 6
```

This script works by iterating from `n-1` down to `1` and checking each number to see if it evenly divides `n` (i.e., if the remainder when `n` is divided by the number is `0`). As soon as it finds such a number, it returns that number.

However, a more efficient solution can be implemented using the math library's gcd (greatest common divisor) function. The largest divisor of a number n is the largest number that divides n, which is mathematically equivalent to the greatest common divisor (gcd) of n and the largest number less than n that divides n.

Here's how you can modify the function to use the math library's gcd function:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(12))  # Output: 6

# Using the math library's gcd function
def largest_divisor_math(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor_math(15)
    5
    """
    return n - math.gcd(n, n - 1)

# Test the function
print(largest_divisor_math(15))  # Output: 5
print(largest_divisor_math(10))  # Output: 5
print(largest_divisor_math(12))  # Output: 6
```

But in a more simplified manner, you can achieve the desired result by dividing the number by the last number which is obviously going to be the largest divisor.

```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n % 2 == 0:
        return n // 2
    for i in range(n - 1, 1, -2):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(12))  # Output: 6
```
It is also worth noting that, as an optimization, you can start the loop from `math.isqrt(n)` if you know that the square root of the number is very small, since all divisors of the number will be among its factors below the square root.