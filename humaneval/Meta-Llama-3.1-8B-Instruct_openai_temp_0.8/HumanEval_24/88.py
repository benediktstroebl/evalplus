```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # If the number is less than 2, there's no divisor
    if n < 2:
        return None
    # Start from n-1 and check for each number if it's a divisor of n
    for i in range(n-1, 1, -1):
        # If n is divisible by i, return i as the largest divisor
        if n % i == 0:
            return i
    # If no divisor is found, return 1 as the largest divisor
    return 1

# Test the function
print(largest_divisor(15))  # Should print: 5
print(largest_divisor(10))  # Should print: 5
print(largest_divisor(7))   # Should print: 1
print(largest_divisor(1))   # Should print: None
```

However, there's a more efficient approach. The largest divisor of a number `n` can be found by checking the factors of `n` from the largest to the smallest without the need to check numbers smaller than the square root of `n`, since a larger factor of `n` must be a multiple of a smaller factor that has already been checked. 

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # If the number is less than 2, there's no divisor
    if n < 2:
        return None
    # Check numbers from n-1 down to the square root of n
    for i in range(n-1, math.isqrt(n)-1, -1):
        # If n is divisible by i, return i as the largest divisor
        if n % i == 0:
            return i
    # If no divisor is found, return 1 as the largest divisor
    return 1

# Test the function
print(largest_divisor(15))  # Should print: 5
print(largest_divisor(10))  # Should print: 5
print(largest_divisor(7))   # Should print: 1
print(largest_divisor(1))   # Should print: None
```

The `math.isqrt(n)` function, available in Python 3.8 and later, returns the integer square root of `n`. This simplifies the code and eliminates the need for manual calculation of the square root.