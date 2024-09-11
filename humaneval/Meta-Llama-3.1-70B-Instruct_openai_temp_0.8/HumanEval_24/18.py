```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start checking from the largest possible divisor, which is n - 1
    for i in range(n - 1, 0, -1):
        # If i is a divisor of n, return it
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that finds the largest divisor of a given number `n`. It iterates from `n - 1` down to 1 and returns the first number that divides `n` evenly. The example usage demonstrates how to call the function with the input 15 and print the result.