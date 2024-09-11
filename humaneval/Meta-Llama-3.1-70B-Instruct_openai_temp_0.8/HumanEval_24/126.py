```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

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
print(largest_divisor(10))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
```

This script works by iterating over all numbers smaller than `n` and checking if `n` is divisible by that number. As soon as it finds a number that divides `n` evenly, it returns that number. This approach ensures that the function always returns the largest divisor, since it starts from the largest possible divisor and moves downwards.