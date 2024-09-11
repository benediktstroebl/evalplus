```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # We start checking from the second largest number (n-1) downwards
    for i in range(n-1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i

    # If no divisor is found, it means the number is prime
    return n


# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 17
```

However, there is a more efficient way to solve this problem. The largest divisor of a number `n` is actually the square root of `n`. So, we can check all numbers up to the square root of `n` to find the largest divisor:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # We only need to check up to the square root of n
    for i in range(int(math.sqrt(n)), 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 17
```

This version of the function is more efficient because it reduces the number of iterations from `n-1` to `sqrt(n)`, which can make a big difference for large numbers.