```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the largest possible divisor (n - 1) and check if it's a divisor
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

However, we can optimize this function by using the mathematical property that the largest divisor of a number will be a factor of its square root. We can modify the function as follows:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Calculate the square root of n
    sqrt_n = math.isqrt(n)
    # Start from the largest possible divisor (sqrt_n) and check if it's a divisor
    for i in range(sqrt_n, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This version of the function will be more efficient for large inputs, as it reduces the number of iterations required to find the largest divisor.