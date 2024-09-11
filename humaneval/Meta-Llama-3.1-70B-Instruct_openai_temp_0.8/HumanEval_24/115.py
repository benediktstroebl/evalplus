```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script works by iterating from `n-1` down to `1` and checking if `i` is a divisor of `n` by using the modulo operator (`%`). If `n % i` equals `0`, then `i` is a divisor of `n`, and the function returns `i`. The loop starts from `n-1` and goes down to `1` to ensure that the function finds the largest divisor of `n`.