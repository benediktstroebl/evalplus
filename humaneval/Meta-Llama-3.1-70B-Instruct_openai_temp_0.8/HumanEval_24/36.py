```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(100)) # Expected output: 50
```

This script defines the `largest_divisor` function, which iterates from `n-1` down to `1` and returns the first number that divides `n` evenly (i.e., the remainder is `0`). The script also includes test cases to demonstrate the function's behavior.