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
        >>> largest_divisor(17)
        1
        >>> largest_divisor(25)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(25))  # Expected output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates over the numbers from `n-1` down to `1` and checks if `n` is divisible by each number using the modulo operator (`%`). As soon as it finds a divisor, it returns that number.

The script also includes test cases to demonstrate the function's correctness.