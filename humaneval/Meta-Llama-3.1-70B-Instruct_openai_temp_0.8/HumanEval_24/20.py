```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(12))  # Expected output: 6
print(largest_divisor(25))  # Expected output: 5
```
This script defines a function `largest_divisor` that iterates from `n-1` down to `1` and returns the first number `i` such that `n` is divisible by `i`. This is the largest divisor of `n` smaller than `n`. The script includes test cases to demonstrate the function's correctness.