```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n.
    """
    # Iterate from n-1 to 1
    for i in range(n - 1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, return i
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script works by iterating from `n-1` to `1`, checking each number to see if it divides `n` evenly (i.e., with no remainder). The first number that does is the largest divisor of `n` that is smaller than `n`, so it is returned.

However, this solution can be optimized further for larger inputs by only checking up to the square root of `n`, since any factor larger than that would have a corresponding factor smaller than the square root.

Here's a more optimized version:

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
    # Iterate from sqrt(n) to 1
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, return the larger of i and n // i
            return max(i, n // i)

# Test the function
print(largest_divisor(15))  # Output: 5
```

This version works similarly, but only checks up to the square root of `n`, making it more efficient for larger inputs.