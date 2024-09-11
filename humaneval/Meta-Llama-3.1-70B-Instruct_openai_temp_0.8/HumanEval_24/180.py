```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest divisor of n, smaller than n.

    Raises:
    ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Input number must be greater than 1")

    # Start checking from the largest possible divisor (n-1) down to 1
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i


# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(25))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function checks all numbers from `n-1` down to `1` to find the largest divisor. If `n` is less than 2, the function raises a `ValueError` because there is no largest divisor for numbers less than or equal to 1.