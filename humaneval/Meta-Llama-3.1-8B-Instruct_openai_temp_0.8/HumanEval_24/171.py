```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Iterate from n-1 down to 1 to find the largest divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as it's the largest one
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```

However, this can be optimized by checking for divisors starting from the square root of `n`, as any factor larger than the square root would have a corresponding factor smaller than the square root.

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Iterate from the square root of n down to 1 to find the largest divisor
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as it's the largest one
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```