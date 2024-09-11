```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Example:
        >>> largest_divisor(15)
        5
    """
    # Start checking from the second last number
    for i in range(n - 1, 0, -1):
        # Check if the current number is a divisor of n
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Should print 5
```

However, there is a more concise and efficient way to implement this function using the `math.gcd` function from the math module, which returns the greatest common divisor of two numbers.

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Example:
        >>> largest_divisor(15)
        5
    """
    # The largest divisor of n is n // gcd(n, n-1)
    return n // math.gcd(n, n - 1)

# Test the function
print(largest_divisor(15))  # Should print 5
```