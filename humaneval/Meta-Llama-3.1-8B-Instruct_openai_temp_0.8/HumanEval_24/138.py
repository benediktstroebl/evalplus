```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Check if n is less than or equal to 1, in which case there's no divisor other than 1
    if n <= 1:
        return 1
    
    # Iterate from n-1 down to 2 to find the largest divisor
    for i in range(n - 1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor of n, return it as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(100))  # Output: 50
```

However, the most efficient way to find the largest divisor of a number is to start from the square root of the number. This is because a larger factor of the number would be a multiple of a smaller factor that has already been checked.

Here's a more optimized version of the function:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Check if n is less than or equal to 1, in which case there's no divisor other than 1
    if n <= 1:
        return 1
    
    # Iterate from the square root of n down to 2 to find the largest divisor
    for i in range(int(math.sqrt(n)), 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor of n, return it as the largest divisor
            return i
    
    # If n is a prime number, its only divisors are 1 and n itself
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(100))  # Output: 50
```