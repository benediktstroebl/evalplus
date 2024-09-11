```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Start checking from n-1 down to 1
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, return i as the largest divisor
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It iterates from `n-1` down to `1` and returns the first number `i` such that `n` is divisible by `i`. The example usage demonstrates the function's behavior with the input `15`, which returns the expected output `5`.