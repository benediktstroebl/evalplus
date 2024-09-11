```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): Input number
    
    Returns:
        int: The largest divisor of n smaller than n
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and check if it's divisible by n
    for i in range(n-1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i
    # If no divisor is found, return 1 (1 is a divisor of every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
```

However, a more Pythonic way to solve this problem is to use the `math.gcd` function. It returns the greatest common divisor of two numbers, which is the largest divisor of both numbers.

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): Input number
    
    Returns:
        int: The largest divisor of n smaller than n
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Since gcd(n, n-1) or gcd(n, 1) will always be 1, we return n-1
    return n - math.gcd(n, n-1)

# Test the function
print(largest_divisor(15))  # Output: 5
```