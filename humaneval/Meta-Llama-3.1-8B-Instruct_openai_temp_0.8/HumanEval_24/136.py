```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Example usage
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function does this by iterating from `n-1` down to `1` and checking each number to see if it divides `n` evenly using the modulo operator (`%`). The first number it finds that divides `n` evenly is the largest divisor, and it returns this number.

The example usage at the end of the script demonstrates how to use the `largest_divisor` function. When you run this script, it will print `5` to the console, which is the largest divisor of `15`.