```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1  # Return 1 in case n is a prime number

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor` that finds the largest divisor of a given number `n` smaller than `n`. It iterates from `n-1` to `1` and checks each number `i` if `n` is divisible by `i`. The first number `i` that divides `n` evenly is the largest divisor. If `n` is a prime number, the function returns `1`. The script includes test cases to demonstrate the function's usage.