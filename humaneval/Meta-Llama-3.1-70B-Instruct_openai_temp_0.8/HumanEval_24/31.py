```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n that is smaller than n.
    """
    # Start checking from the largest possible divisor, which is n-1
    for i in range(n-1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If i divides n evenly, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

Alternatively, you can use a more efficient approach by iterating only up to the square root of `n`:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n that is smaller than n.
    """
    # Iterate from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        # Check if i divides n evenly
        if n % i == 0:
            # If i divides n evenly, return the larger divisor (either i or n//i)
            return max(i, n // i)
    # If no divisors are found, return 1
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(17))  # Output: 1
```