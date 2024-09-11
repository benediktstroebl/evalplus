```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.
    """
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    # Start from n - 1 and decrement by 1 until we find a divisor
    for i in range(n - 1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            return i

    # If no divisor is found, return None
    return None

# Example usage
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes a positive integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple iterative approach, starting from `n - 1` and decrementing by 1 until it finds a divisor. If no divisor is found (which should not happen for positive integers), the function returns `None`.

You can run this script and test the `largest_divisor` function with different inputs to see its behavior.