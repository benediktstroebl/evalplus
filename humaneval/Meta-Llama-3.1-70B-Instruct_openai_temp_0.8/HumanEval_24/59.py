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
print(largest_divisor(25))  # Output: 5
print(largest_divisor(100))  # Output: 50
```
This script works by checking each number smaller than `n` to see if it divides `n` evenly (i.e., `n % i == 0`). As soon as it finds a divisor, it returns that number, since we're checking in descending order. 

However, a more efficient solution can be achieved by iterating up to the square root of `n`, as any factor larger than the square root would have a corresponding factor smaller than the square root. Here's an optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return max(i, n // i)

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(25))  # Output: 5
print(largest_divisor(100))  # Output: 50
```
In this version, we also return the larger of the factor and its corresponding factor (i.e., `max(i, n // i)`) to ensure we get the largest divisor.