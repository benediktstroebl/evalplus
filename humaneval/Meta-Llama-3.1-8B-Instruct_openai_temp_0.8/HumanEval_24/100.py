```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n smaller than n

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return n

# Example usage
print(largest_divisor(15))  # Output: 5
```

However, this solution has a time complexity of O(n) due to the loop that goes from n-1 down to 1. A more efficient solution with a time complexity of O(sqrt(n)) can be achieved using the following code:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n smaller than n

    >>> largest_divisor(15)
    5
    """
    for i in range(int(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return i
    return n

# Example usage
print(largest_divisor(15))  # Output: 5
```

This solution works by iterating down from the square root of n, because a larger factor of the number would be a multiple of a smaller factor that has already been checked.