```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n.
    """
    # We start checking from n-1 because the problem statement asks for a divisor smaller than n
    for i in range(n-1, 0, -1):
        # If n is divisible by i, then i is a divisor of n
        if n % i == 0:
            # Since we're checking in descending order, the first divisor we find will be the largest
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns its largest divisor smaller than `n`. It does this by checking all numbers from `n-1` down to 1 to see if they divide `n` evenly. The first number it finds that does so is the largest divisor of `n`, which it then returns.

Alternatively, you can also solve this problem more efficiently by only checking up to the square root of `n`, as any factor larger than the square root would have a corresponding factor smaller than the square root.

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n.
    """
    # We start checking from the square root of n
    for i in range(int(math.sqrt(n)), 0, -1):
        # If n is divisible by i, then i is a divisor of n
        if n % i == 0:
            # We return the larger of i and n // i, because n // i is also a divisor
            return max(i, n // i)

# Test the function
print(largest_divisor(15))  # Output: 5
```