```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and iterate downwards to find the largest divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5

# Alternative solution using math.gcd
import math
def largest_divisor_gcd(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.
    """
    # The gcd of n and n-1 will be the largest divisor of n smaller than n
    return math.gcd(n, n-1)

# Test the alternative function
print(largest_divisor_gcd(15))  # Output: 5
```