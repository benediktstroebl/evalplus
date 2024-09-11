```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for

    Returns:
        int: The largest divisor of n, smaller than n
    """
    # Start checking from the largest possible divisor, which is n - 1
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating over the numbers from `n - 1` down to `1`, and returning the first number it finds that divides `n` evenly. The example usage at the end shows how to call the function with the input `15`, which returns the expected output `5`.