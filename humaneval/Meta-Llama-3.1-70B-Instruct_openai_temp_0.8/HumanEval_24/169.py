```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Example:
    >>> largest_divisor(15)
    5
    """
    # Start checking from n-1, because n itself will always divide n
    for i in range(n-1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If i divides n evenly, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

Alternatively, you can also use a more mathematical approach to solve this problem, which is to find the second largest factor of `n`. Here is how you can do it:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Example:
    >>> largest_divisor(15)
    5
    """
    # Find the square root of n
    sqrt_n = math.isqrt(n)
    
    # Start checking from sqrt_n, because a larger factor of n must be a multiple of a smaller factor that has already been checked
    for i in range(sqrt_n, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If i divides n evenly, return n // i as the largest divisor
            # We can't return i, because i may be the square root of n, in which case n // i would be the same as i
            return n // i

# Test the function
print(largest_divisor(15))  # Output: 5
```