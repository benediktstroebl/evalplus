```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Raises:
        ValueError: If n is less than 1.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
    """
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")

    # Start checking from n - 1 downwards, since we know n is not a divisor of itself
    for i in range(n - 1, 0, -1):
        # If n is divisible by i with no remainder, i is a divisor of n
        if n % i == 0:
            # Since we're checking in descending order, the first divisor we find will be the largest
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

You can also write a more concise version using the `math.gcd` function, which returns the greatest common divisor of two numbers. Since the greatest common divisor of `n` and any number less than `n` that divides `n` will be that number itself, we can use this function to find the largest divisor:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Raises:
        ValueError: If n is less than 1.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
    """
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")

    # Start checking from n - 1 downwards
    for i in range(n - 1, 0, -1):
        if math.gcd(n, i) == i:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```