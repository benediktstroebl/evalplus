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
    return 1  # Return 1 as the largest divisor for prime numbers

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(24))  # Expected output: 12
```

This Python script defines a function `largest_divisor` that finds the largest number smaller than the input `n` that divides `n` evenly. The function iterates from `n - 1` down to 1 and returns the first number that divides `n` evenly. For prime numbers, the largest divisor is 1, so the function returns 1 in such cases. The script also includes test cases to demonstrate the function's behavior.