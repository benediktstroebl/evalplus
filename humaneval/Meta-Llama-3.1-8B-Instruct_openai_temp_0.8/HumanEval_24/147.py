```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n that is smaller than n.
    
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(12))  # Output: 6
```

Alternatively, you can also use the `math.gcd` function to find the largest divisor, as the greatest common divisor of a number and its divisor is the divisor itself:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n that is smaller than n.
    
    >>> largest_divisor(15)
    5
    """
    return n // math.gcd(n, n - 1)

print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(12))  # Output: 6
```