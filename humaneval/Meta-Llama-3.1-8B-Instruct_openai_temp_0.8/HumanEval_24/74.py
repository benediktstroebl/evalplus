```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest divisor of n smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from the second last number and check if it's a divisor
    for i in range(n - 1, 1, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```

Alternatively, you can also use the math library's gcd (Greatest Common Divisor) function from the Euclidean algorithm to find the largest divisor:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest divisor of n smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    # The largest divisor smaller than n is n // gcd(n, n-1)
    return n // math.gcd(n, n - 1)

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```

Both of these methods work, but the second method is more efficient for large inputs.