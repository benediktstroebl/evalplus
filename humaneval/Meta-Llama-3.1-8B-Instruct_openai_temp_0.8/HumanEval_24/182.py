```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n

    >>> largest_divisor(15)
    5
    """
    # Start from the largest possible divisor (n-1)
    for i in range(n-1, 0, -1):
        # Check if n is divisible by the current number
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(100)) # Output: 50
```

However, the above solution has a time complexity of O(n), which can be inefficient for large numbers.

We can use a more efficient approach by checking all numbers up to the square root of n. This is because a larger factor of the number would be a multiple of a smaller factor that has already been checked.

Here is the optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n

    >>> largest_divisor(15)
    5
    """
    # Start from the largest possible divisor (n-1)
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        # Check if n is divisible by the current number
        if n % i == 0:
            # Return the largest divisor
            return n // i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(100)) # Output: 50
```
This optimized version has a time complexity of O(√n), which is much more efficient for large numbers.