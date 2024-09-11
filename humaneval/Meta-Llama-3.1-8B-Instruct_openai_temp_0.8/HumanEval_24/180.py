```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        int: The largest divisor of n that is smaller than n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1  # Return 1 if n is prime

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(17))  # Should print 1
print(largest_divisor(24))  # Should print 12
```

However, it's worth noting that there's an even more efficient way to solve this problem. We can iterate from 2 to the square root of n and check if n is divisible by any of these numbers. If it is, then the largest divisor smaller than n would be n divided by the current divisor. Here's how you can implement it:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        int: The largest divisor of n that is smaller than n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return n // i
    return 1  # Return 1 if n is prime

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(17))  # Should print 1
print(largest_divisor(24))  # Should print 12
```

This version of the function is more efficient because it stops iterating as soon as it finds a divisor. It also handles the case where n is prime (i.e., where the largest divisor smaller than n is 1) in a more elegant way.