```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest number that divides n evenly, smaller than n.
    """
    # Start checking from n-1, since n itself is not considered
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5

# Additional test cases
print(largest_divisor(17))  # Output: 1 (since 17 is prime)
print(largest_divisor(24))  # Output: 12
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It uses a simple iterative approach, starting from `n-1` and moving downwards to find the largest divisor.