```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n, smaller than n.
    """
    if n < 2:
        raise ValueError("Input number must be greater than 1")

    # Start checking from n-1 downwards
    for i in range(n - 1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            return i

    # If no divisor is found, return None
    return None


# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(25))  # Expected output: 5
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number smaller than `n` that divides `n` evenly. The function uses a simple iterative approach, checking all numbers from `n-1` down to 1 to see if they divide `n` evenly. The function raises a `ValueError` if `n` is less than 2.