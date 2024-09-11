```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The number to find the largest divisor for.
    
    Returns:
        int: The largest divisor of n, smaller than n.
    """
    # Start checking from the largest possible divisor (n-1)
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

However, this solution can be optimized for larger inputs by only checking up to the square root of n, as any factor larger than this would have a corresponding factor smaller than the square root. Here's an optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The number to find the largest divisor for.
    
    Returns:
        int: The largest divisor of n, smaller than n.
    """
    # Start checking from the largest possible divisor (sqrt(n))
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return the larger divisor
            return n // i

# Example usage:
print(largest_divisor(15))  # Output: 5
```