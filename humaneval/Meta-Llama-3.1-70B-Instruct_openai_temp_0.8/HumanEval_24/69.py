```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.
    """
    # Check if the input is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    # Start from n-1 and go down to 1 to find the largest divisor
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It uses a simple iterative approach, starting from `n-1` and going down to `1`, to find the largest divisor. The script also includes a test case to demonstrate the function's usage.