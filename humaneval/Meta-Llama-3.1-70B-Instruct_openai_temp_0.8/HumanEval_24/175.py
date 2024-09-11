```python
def largest_divisor(n: int) -> int:
    """
    This function finds the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number for which to find the largest divisor.

    Returns:
        int: The largest number that divides n evenly, smaller than n.
    """
    # Start checking from n-1, because n cannot divide n evenly
    for i in range(n - 1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, return i as the largest divisor
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It iterates from `n-1` down to `1`, checks if each number divides `n` evenly, and returns the first one that does. The function includes a docstring with a description, arguments, and return value information, as well as an example usage at the end.