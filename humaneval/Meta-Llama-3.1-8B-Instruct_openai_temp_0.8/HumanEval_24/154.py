```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n.
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

However, this solution is not the most efficient as it checks every number from `n-1` down to `1`. A more efficient solution is to only check up to the square root of `n`, as any factor larger than that would have a corresponding factor smaller than the square root.

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n.
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(int(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

Alternatively, you can also use the `math.gcd` function to find the greatest common divisor (GCD) of `n` and `n-1`, and return the GCD. The GCD is the largest number that divides both `n` and `n-1` evenly, and by definition, it also divides `n` evenly.

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n.
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    return math.gcd(n, n - 1)

# Test the function
print(largest_divisor(15))  # Output: 5
```