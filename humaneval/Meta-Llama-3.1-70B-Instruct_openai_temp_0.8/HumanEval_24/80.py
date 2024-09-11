```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.
    """
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that iterates from `n-1` down to `2` and returns the first number that divides `n` evenly (i.e., with no remainder). This is the largest number that divides `n` evenly and is smaller than `n`.

However, this solution is not efficient for large numbers. Here's a more efficient version:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.
    """
    for i in range(int(n**0.5) + 1, 1, -1):
        if n % i == 0:
            return max(i, n // i)

# Test the function
print(largest_divisor(15))  # Output: 5
```

This version only checks up to the square root of `n`, because a larger factor of `n` would be a multiple of a smaller factor that has already been checked. If `n` is divisible by `i`, it returns the maximum of `i` and `n // i`, which is the largest divisor.