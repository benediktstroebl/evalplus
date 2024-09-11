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

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines the `largest_divisor` function as specified. It works by iterating over the numbers from `n - 1` down to `1` and returning the first number that divides `n` evenly (i.e., leaves no remainder). This is the largest number smaller than `n` that divides `n` evenly.

The example usage at the end demonstrates how to use the function and verifies that it produces the expected output for the given example.