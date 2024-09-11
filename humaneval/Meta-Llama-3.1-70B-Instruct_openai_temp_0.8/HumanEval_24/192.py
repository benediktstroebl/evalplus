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
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating over all numbers from `n-1` down to 1, and returning the first number that divides `n` with a remainder of 0.

The script also includes some test cases to verify the correctness of the function.