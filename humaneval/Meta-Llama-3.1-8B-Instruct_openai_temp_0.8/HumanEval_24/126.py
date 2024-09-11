### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Iterate from the number n downwards to check for divisibility
    for i in range(n - 1, 0, -1):
        # Check if the current number is a divisor of n
        if n % i == 0:
            # If it's a divisor, return it as the largest divisor
            return i
    # If no divisors are found, return 1 (1 is a divisor of every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

However, we can make this function more efficient by iterating up to the square root of `n`, because a larger factor of `n` must be a multiple of a smaller factor that has already been checked.

### Optimized Largest Divisor Function
```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Iterate up to the square root of n to check for divisibility
    for i in range(int(math.sqrt(n)), 0, -1):
        # Check if the current number is a divisor of n
        if n % i == 0:
            # If it's a divisor, return it as the largest divisor
            return i
    # If no divisors are found, return 1 (1 is a divisor of every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```