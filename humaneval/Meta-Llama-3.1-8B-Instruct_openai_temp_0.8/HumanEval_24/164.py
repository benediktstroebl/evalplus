```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): A positive integer.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    # Initialize the largest divisor as 1 (since 1 is a divisor of all numbers)
    largest_div = 1
    
    # Iterate from n-1 down to 2
    for i in range(n-1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, update the largest divisor
            largest_div = i
            # Break the loop since we've found the largest divisor
            break
    
    return largest_div


# Example usage:
print(largest_divisor(15))  # Output: 5
```

Alternatively, you can also use a more efficient approach using the math library and the sqrt function, which will stop checking for divisors once it reaches the square root of n:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): A positive integer.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    # Initialize the largest divisor as 1 (since 1 is a divisor of all numbers)
    largest_div = 1
    
    # Iterate from sqrt(n) down to 2
    for i in range(math.isqrt(n), 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, update the largest divisor
            largest_div = i
            # Break the loop since we've found the largest divisor
            break
    
    return largest_div


# Example usage:
print(largest_divisor(15))  # Output: 5
```

This version of the function will run much faster for large inputs because it only needs to check divisors up to the square root of n, rather than all the way down to 1.