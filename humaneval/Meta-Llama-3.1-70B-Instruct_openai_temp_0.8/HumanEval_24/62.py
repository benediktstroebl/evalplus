```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n that is smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
    """
    # Start from the largest possible divisor, which is n-1
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides `n` evenly and is smaller than `n`. The function iterates from `n-1` down to `1` and checks each number to see if it is a divisor of `n`. The first divisor it finds is the largest one, so it returns that number.

You can run this script to test the `largest_divisor` function with different inputs.