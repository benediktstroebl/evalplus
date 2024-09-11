```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Raises:
        ValueError: If n is less than 2.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
    """
    if n < 2:
        raise ValueError("Input number should be greater than 1")

    # Start checking from n-1 down to 1
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

Alternatively, you can also solve this problem more efficiently by only checking up to the square root of n, since a larger factor of n would be a multiple of a smaller factor that has already been checked.

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Raises:
        ValueError: If n is less than 2.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
    """
    if n < 2:
        raise ValueError("Input number should be greater than 1")

    # Start checking from n-1 down to 1
    for i in range(n - 1, math.isqrt(n), -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

    # If no divisors are found, return 1
    return 1

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```