```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # We start checking from the largest possible divisor, which is n-1
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple iterative approach, starting from `n-1` and checking each number to see if it divides `n` evenly. The first number that meets this condition is returned as the result.

Note that this function assumes that the input `n` is a positive integer. If `n` is not positive or not an integer, the function may not work correctly. You may want to add error checking to handle these cases if necessary.