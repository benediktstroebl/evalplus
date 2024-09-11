```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n, smaller than n
    """
    # Start from n-1 and decrement until we find a divisor
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i


# Test the function
print(largest_divisor(15))  # Expected output: 5
```

This script starts from `n-1` and decrements until it finds a divisor of `n`. As soon as it finds a divisor, it returns that divisor, since it's the largest possible divisor smaller than `n`. The time complexity of this solution is O(n), which might not be efficient for large inputs. If you need a more efficient solution, you can consider iterating up to the square root of `n`, which would reduce the time complexity to O(sqrt(n)). 

Here's how you can do that:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n, smaller than n
    """
    # Start from the square root of n and decrement until we find a divisor
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Return the larger divisor (i or n//i)
            return max(i, n // i)


# Test the function
print(largest_divisor(15))  # Expected output: 5
```