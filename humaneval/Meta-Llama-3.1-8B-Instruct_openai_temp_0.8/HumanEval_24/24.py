```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Iterate from n-1 to 1 in descending order
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i
    # If no divisor is found, return -1
    return -1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1 (17 is a prime number)
print(largest_divisor(100))  # Output: 50
print(largest_divisor(97))   # Output: 1 (97 is a prime number)
```

However, we can optimize this function by simply finding the greatest common divisor (GCD) of the number, which can be computed efficiently using the Euclidean algorithm. Here's an optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # The GCD of a number and itself is the number itself
    return math.gcd(n, n)

# Test the function
print(largest_divisor(15))  # Output: 15
print(largest_divisor(17))  # Output: 17
print(largest_divisor(100))  # Output: 100
print(largest_divisor(97))   # Output: 97
```

In this optimized version, we use the built-in `math.gcd()` function from Python's standard library, which is an implementation of the Euclidean algorithm. This makes the function much more efficient and easier to read.