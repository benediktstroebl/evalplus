```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start checking from the largest possible divisor, which is n-1
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script works by iterating over all numbers smaller than `n` in descending order, and checking if they are divisors of `n` by using the modulus operator (`%`). The first number that is a divisor of `n` is the largest one, so it is returned immediately.

Alternatively, you can use a more efficient approach by only checking up to the square root of `n`, as any factor larger than that would have a corresponding factor smaller than the square root. Here's how you can implement it:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start checking from the largest possible divisor, which is the square root of n
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return the larger of i and n//i as the largest divisor
            return max(i, n//i)

# Test the function
print(largest_divisor(15))  # Output: 5
```

This version of the function is more efficient for large inputs, as it reduces the number of iterations from `n` to approximately `sqrt(n)`.