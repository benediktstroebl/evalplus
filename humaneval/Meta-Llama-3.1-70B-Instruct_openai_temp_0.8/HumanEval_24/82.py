```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n that is smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """

    # Start from n-1 and go down to 1 to find the largest divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```
This script works by iterating over all numbers less than `n` and checking if they divide `n` evenly. The first number it finds that divides `n` evenly is the largest divisor of `n` that is smaller than `n`. 

However, it's worth noting that this solution is not the most efficient for large numbers, as it checks every number less than `n`. A more efficient solution would be to only check up to the square root of `n`, as any factor larger than that would have a corresponding factor smaller than the square root. Here is an optimized version of the function:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n that is smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """

    # Start from sqrt(n) and go down to 1 to find the largest divisor
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return the larger of i and n//i as the largest divisor
            return max(i, n//i)

# Test the function
print(largest_divisor(15))  # Output: 5
```
This optimized version works the same way as the previous one, but it only checks up to the square root of `n`, making it much faster for large numbers.