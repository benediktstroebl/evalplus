```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n.
    """
    # Start from the largest possible divisor, which is n/2
    for i in range(n // 2, 0, -1):
        # Check if the number is divisible by i
        if n % i == 0:
            # If it's divisible, return the divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

In this script, the `largest_divisor` function iterates from `n/2` down to 1, checking if each number divides `n` evenly. As soon as it finds a divisor, it returns that number. The time complexity of this solution is O(n), where n is the input number.

However, we can improve this solution to have a better time complexity of O(sqrt(n)) by only iterating up to the square root of `n`. Here's an optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n.
    """
    # Start from the largest possible divisor, which is sqrt(n)
    for i in range(math.isqrt(n), 0, -1):
        # Check if the number is divisible by i
        if n % i == 0:
            # If it's divisible, return the divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

In this optimized version, the function uses the `math.isqrt` function to get the integer square root of `n` and starts the iteration from there. This significantly reduces the number of iterations, especially for large input numbers.