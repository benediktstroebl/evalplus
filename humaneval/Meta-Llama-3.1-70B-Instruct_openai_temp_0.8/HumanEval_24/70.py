```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    Raises:
    ValueError: If n is less than 1.

    >>> largest_divisor(15)
    5
    """
    if n < 1:
        raise ValueError("Input number should be greater than or equal to 1")

    # Start checking from n-1, as we need a divisor smaller than n
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(25))  # Output: 5
```

This script defines a function `largest_divisor` that finds the largest divisor of a given number `n`, smaller than `n`. It uses a simple iterative approach, checking numbers from `n-1` down to `1` to find the first one that divides `n` evenly. The function includes error handling and docstrings for clarity.