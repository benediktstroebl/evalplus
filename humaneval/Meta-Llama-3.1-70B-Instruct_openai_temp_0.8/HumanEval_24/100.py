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

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(24))  # Expected output: 12
print(largest_divisor(37))  # Expected output: 1
```

Explanation:

*   The `largest_divisor` function takes an integer `n` as input and returns its largest divisor smaller than `n`.
*   The function iterates over numbers from `n-1` down to `1`.
*   For each number `i`, it checks if `n` is divisible by `i` using the modulo operator (`n % i == 0`).
*   As soon as it finds a number that divides `n` evenly, it returns that number as the largest divisor.
*   The test cases demonstrate the function's correctness for different inputs.