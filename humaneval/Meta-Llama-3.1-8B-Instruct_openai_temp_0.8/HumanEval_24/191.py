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
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(16))  # Expected output: 8
print(largest_divisor(17))  # Expected output: 1
```

This script defines a function `largest_divisor(n)` that finds the largest number smaller than `n` that divides `n` evenly. It does this by iterating from `n - 1` downwards and checking each number to see if it divides `n` evenly. As soon as it finds a number that does, it returns that number.

Alternatively, you can also use the `math.gcd` function in combination with the fact that `a * b = gcd(a, b) * lcm(a, b)` to find the largest divisor. However, this approach is more complex and may not be necessary unless you need to handle very large numbers.

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return n // math.gcd(n, n - 1)

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(16))  # Expected output: 8
print(largest_divisor(17))  # Expected output: 1
```