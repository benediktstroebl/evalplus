```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): A positive integer.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the second largest number (n-1), and check if it's a divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return the largest divisor
            return i
    # If no divisors are found, return 1
    return 1

# Test the function
print(largest_divisor(15))  # Expected output: 5
```

However, the above implementation has a time complexity of O(n), which can be optimized to O(sqrt(n)) by only checking up to the square root of n. This is because a larger factor of n would be a multiple of a smaller factor that has already been checked.

Here is the optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): A positive integer.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the largest number that could be a divisor
    # which is the square root of n
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return the largest divisor
            return i
    # If no divisors are found, return 1
    return 1

# Test the function
print(largest_divisor(15))  # Expected output: 5
```

This optimized version has a significant performance improvement for large inputs.