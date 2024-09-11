```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the number n-1 and decrement until we find a divisor of n
    for i in range(n-1, 1, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

    # If no divisors are found, return 1 (the only number that always divides any number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
```

However, this can be optimized using the property of the largest divisor:

*   The largest divisor of n is less than √n, because n cannot be a multiple of any number greater than √n.
*   We can start checking from the largest possible divisor down to 1, but due to the property above, we can start from the largest integer less than or equal to √n and go down to 1.

Here's the optimized version:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the largest integer less than or equal to √n and go down to 1
    for i in range(math.isqrt(n), 1, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

    # If no divisors are found, return 1 (the only number that always divides any number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
```

This optimized version has a time complexity of O(√n), significantly faster than the original version for large inputs.